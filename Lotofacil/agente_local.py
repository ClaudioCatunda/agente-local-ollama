import os
import httpx
import json
import chromadb     

# 1. FUNÇÃO: Mapeador do Hardware
def listar_arquivos_locais(subpasta: str) -> list:
    RAIZ_SEGURA = "/Volumes/Catunda_SSD/Developer/Documents"
    subpasta_limpa = subpasta.strip()
    
    if subpasta_limpa in ["", ".", "/", "./", "Documents", "./Documents"]:
        caminho_completo = RAIZ_SEGURA
    else:
        caminho_completo = os.path.abspath(os.path.join(RAIZ_SEGURA, subpasta_limpa))
    
    if not caminho_completo.startswith(RAIZ_SEGURA):
        return ["Erro: Acesso negado. Fora dos limites permitidos."]
    
    try:
        if os.path.exists(caminho_completo):
            return os.listdir(caminho_completo)
        else:
            return [f"Erro: A pasta '{subpasta_limpa}' não foi encontrada."]
    except Exception as e:
        return [f"Erro ao ler pasta: {str(e)}"]

# 2. FUNÇÃO: Leitor Seguro de Arquivos
def ler_conteudo_arquivo(nome_arquivo: str) -> str:
    RAIZ_SEGURA = "/Volumes/Catunda_SSD/Developer/Documents"
    caminho_completo = os.path.abspath(os.path.join(RAIZ_SEGURA, nome_arquivo))
    
    if not caminho_completo.startswith(RAIZ_SEGURA):
        return "Erro: Acesso negado. Arquivo fora dos limites permitidos."
    
    try:
        if os.path.exists(caminho_completo) and os.path.isfile(caminho_completo):
            with open(caminho_completo, 'r', encoding='utf-8') as f:
                # Truncamento preventivo para preservar o contexto do modelo menor
                conteudo = f.read(4096)
                if len(conteudo) == 4096:
                    conteudo += "\n\n[... Conteúdo truncado via Python para otimização de contexto ...]"
                return conteudo
        else:
            return f"Erro: O arquivo '{nome_arquivo}' não foi encontrado."
    except Exception as e:
        return f"Erro ao ler arquivo: {str(e)}"
    
# 3. INTERFACE DETERMINÍSTICA (ORQUESTRADA VIA PYTHON)
OLLAMA_URL = "http://localhost:11434/api/chat"
#MODELO_LOCAL = "llama3.2:latest"
MODELO_LOCAL = "qwen2.5:14b"

def executar_fluxo_agente(pergunta_usuario):
    RAIZ_SEGURA = "/Volumes/Catunda_SSD/Developer/Documents"
    CHROMA_PATH = "/Volumes/Catunda_SSD/Developer/Lotofacil/chroma_db"
    MAPA_JSON_PATH = os.path.join(RAIZ_SEGURA, "mapa_conhecimento.json")
    
    conteudo_contexto = ""
    
    # Passo 1: Tentativa de Busca Semântica no Banco Vetorial (RAG)
    try:
        # Geramos o embedding da pergunta do usuário usando o modelo local do Ollama
        response_embed = httpx.post("http://localhost:11434/api/embeddings", json={
            "model": "nomic-embed-text:latest",
            "prompt": pergunta_usuario
        }, timeout=15.0)
        
        if response_embed.status_code == 200:
            vetor_pergunta = response_embed.json().get("embedding")
            
            # Conecta ao ChromaDB no SSD de forma silenciosa
            cliente_chroma = chromadb.PersistentClient(path=CHROMA_PATH)
            colecao = cliente_chroma.get_collection(name="documentos_developer")
            
            # Busca os 4 pedaços de texto semanticamente mais próximos à pergunta
            resultados_vetoriais = colecao.query(
                query_embeddings=[vetor_pergunta],
                n_results=8
            )
            
            documentos_encontrados = resultados_vetoriais.get("documents", [[]])[0]
            metadados_encontrados = resultados_vetoriais.get("metadatas", [[]])[0]
            
            if documentos_encontrados and len(documentos_encontrados) > 0:
                print(f"   [Sistema]: 🎯 Recuperação Vetorial Ativa (RAG). Localizados {len(documentos_encontrados)} fragmentos relevantes.")
                for doc, meta in zip(documentos_encontrados, metadados_encontrados):
                    conteudo_contexto += f"\n--- Trecho extraído de {meta.get('fonte')} ---\n{doc}\n"
    except Exception as e:
        # Se o banco vetorial falhar ou ainda não tiver dados, o sistema ignora silenciosamente
        pass

    # Passo 2: Fallback Seguro para Metadados (Se o RAG não trouxer dados relevantes)
    if not conteudo_contexto.strip():
        print(f"   [Sistema]: Usando otimização por mapa de conhecimento.")
        if os.path.exists(MAPA_JSON_PATH):
            try:
                with open(MAPA_JSON_PATH, 'r', encoding='utf-8') as f:
                    mapa_conteudo = json.load(f).get("arquivos", {})
                    conteudo_contexto = f"Resumo dos metadados do SSD: {json.dumps(mapa_conteudo, ensure_ascii=False)}"
            except:
                conteudo_contexto = "Nenhum dado contextual disponível no momento."

    try:
    # Passo 3: Geração da Resposta com STREAMING (Velocidade Máxima)
        prompt_final = [
            {
                "role": "system",
                "content": "Você é um assistente de engenharia de software e infraestrutura. Responda à pergunta baseando-se estritamente nos dados reais fornecidos. Seja técnico, direto e formate as saídas com Markdown estruturado."
            },
            {
                "role": "user",
                "content": f"Contexto extraído do SSD:\n{conteudo_contexto}\n\nPergunta do Usuário: {pergunta_usuario}"
            }
        ]
        
        # Usamos httpx.stream em vez de httpx.post comum
        with httpx.stream("POST", OLLAMA_URL, json={
            "model": MODELO_LOCAL,
            "messages": prompt_final,
            "stream": True # Ativamos o streaming no Ollama
        }, timeout=60.0) as r:
            
            resposta_completa = ""
            print("\nAgente 🤖: ", end="", flush=True)
            
            # Lê os fragmentos de texto conforme o Ollama vai gerando
            for line in r.iter_lines():
                if line:
                    dados_linha = json.loads(line)
                    conteudo_fragmento = dados_linha.get("message", {}).get("content", "")
                    print(conteudo_fragmento, end="", flush=True)
                    resposta_completa += conteudo_fragmento
            print() # Quebra de linha final
            
        return resposta_completa
        
    except Exception as e:
        print(f"\nErro ao processar resposta: {e}")
        return ""

# 4. EXECUÇÃO DO LOOP DO CHAT CLEAN (ADAPTADO PARA STREAMING)
print("===========================================================")
print("🤖 AGENTE LOCAL DETERMINÍSTICO - MOTOR RAG COM STREAMING")
print("Digite sua pergunta ou 'sair' para encerrar.")
print("===========================================================")

historico_global = [
    {
        "role": "system",
        "content": "Você é um assistente de organização. Responda à pergunta do usuário baseando-se estritamente nos dados reais fornecidos. Seja claro, direto e conciso."
    }
]

while True:
    try:
        entrada = input("\nVocê 👤: ")
        if entrada.lower() in ["sair", "exit", "quit"]:
            print("Sessão encerrada. Até logo! 🚪")
            break
            
        if not entrada.strip():
            continue
            
        print("\n[Agente Processando...]")
        
        # O streaming agora acontece DENTRO da função executar_fluxo_agente
        resposta = executar_fluxo_agente(entrada)
        
        print("\n-----------------------------------------------------------")
        
        # GESTÃO DE MEMÓRIA (Janela Deslizante)
        if resposta:
            historico_global.append({"role": "user", "content": entrada})
            historico_global.append({"role": "assistant", "content": resposta})
            if len(historico_global) > 5:
                historico_global = [historico_global[0]] + historico_global[-4:]
            
    except KeyboardInterrupt:
        print("\nSessão encerrada via teclado. 🚪")
        break
    except Exception as e:
        print(f"Erro inesperado no loop do chat: {e}")
        break