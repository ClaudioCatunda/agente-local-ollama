import os
import httpx
import json

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
MODELO_LOCAL = "llama3.2:latest"

def executar_fluxo_agente(pergunta_usuario):
    # Passo 1: O Python coleta os dados do hardware diretamente
    arquivos_reais = listar_arquivos_locais(".")
    
    # Passo 2: O Llama atua como classificador/extrator estrito
    prompt_selecao = (
        f"Você é um classificador estrito. O usuário fez a seguinte pergunta: '{pergunta_usuario}'\n"
        f"Os arquivos reais disponíveis no SSD são: {arquivos_reais}\n"
        "Identifique se a pergunta exige a leitura de algum desses arquivos para ser respondida.\n"
        "Se sim, responda estritamente com o nome exato do arquivo encontrado na lista (ex: plano_estudos.txt).\n"
        "Se a pergunta for genérica, apenas uma listagem, ou não precisar ler nenhum arquivo, responda apenas: NENHUM"
    )
    
    try:
        res_selecao = httpx.post(OLLAMA_URL, json={
            "model": MODELO_LOCAL, 
            "messages": [{"role": "user", "content": prompt_selecao}],
            "stream": False
        }, timeout=30.0)
        
        decisao_modelo = res_selecao.json().get("message", {}).get("content", "").strip()
        
        # O Python avalia a decisão com base nos arquivos reais
        conteudo_contexto = ""
        if decisao_modelo in arquivos_reais:
            print(f"   [Sistema]: Extraindo conteúdo real de '{decisao_modelo}'...")
            conteudo_contexto = ler_conteudo_arquivo(decisao_modelo)
        else:
            print(f"   [Sistema]: Processando consulta geral de arquivos.")
            conteudo_contexto = f"Lista de arquivos reais no SSD: {arquivos_reais}"
            
        # Passo 3: Geração da resposta final em texto livre baseada em fatos injetados
        prompt_final = [
            {
                "role": "system",
                "content": "Você é um assistente de organização. Responda à pergunta do usuário baseando-se estritamente nos dados reais fornecidos. Não mencione arquivos que não estão presentes nos dados injetados."
            },
            {
                "role": "user",
                "content": f"Dados extraídos do SSD:\n{conteudo_contexto}\n\nPergunta do Usuário: {pergunta_usuario}"
            }
        ]
        
        res_final = httpx.post(OLLAMA_URL, json={
            "model": MODELO_LOCAL,
            "messages": prompt_final,
            "stream": False
        }, timeout=60.0)
        
        return res_final.json().get("message", {}).get("content", "").strip()
        
    except Exception as e:
        return f"Erro ao processar fluxo: {e}"

# 4. EXECUÇÃO DO LOOP DO CHAT CLEAN
print("===========================================================")
print("🤖 AGENTE LOCAL DETERMINÍSTICO - CONTROLADOR DO DOCUMENTS")
print("Digite sua pergunta ou 'sair' para encerrar.")
print("===========================================================")

while True:
    try:
        entrada = input("\nVocê 👤: ")
        if entrada.lower() in ["sair", "exit", "quit"]:
            print("Sessão encerrada. Até logo! 🚪")
            break
            
        if not entrada.strip():
            continue
            
        print("\n[Agente Processando...]")
        resposta = executar_fluxo_agente(entrada)
        print(f"\nAgente 🤖:\n{resposta}")
        print("\n-----------------------------------------------------------")
        
    except KeyboardInterrupt:
        print("\nSessão encerrada via teclado. 🚪")
        break
    except Exception as e:
        print(f"Erro inesperado no loop do chat: {e}")
        break