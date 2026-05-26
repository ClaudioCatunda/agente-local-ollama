import os
import httpx
import json
from datetime import datetime

RAIZ_SEGURA = "/Volumes/Catunda_SSD/Developer/Documents"
OLLAMA_URL = "http://localhost:11434/api/chat"
MODELO_LOCAL = "llama3.2:latest"
MAPA_JSON_PATH = os.path.join(RAIZ_SEGURA, "mapa_conhecimento.json")

def extrair_metadados_com_ia(nome_arquivo, conteudo):
    """Usa o LLM como um extrator de entidades puro e estrito."""
    prompt = (
        f"Analise o conteúdo do arquivo '{nome_arquivo}' e extraia os metadados exatamente no formato JSON especificado.\n\n"
        f"Conteúdo do arquivo:\n{conteudo[:2000]}\n\n"  # Enviamos apenas o começo para otimizar
        "Sua resposta DEVE ser um JSON estrito com esta estrutura, sem texto extra antes ou depois:\n"
        "{\n"
        "  \"categoria\": \"String curta com o tema principal\",\n"
        "  \"tags\": [\"tag1\", \"tag2\", \"tag3\"],\n"
        "  \"resumo_executivo\": \"Um resumo de apenas uma linha do objetivo do arquivo.\"\n"
        "}"
    )
    
    try:
        response = httpx.post(OLLAMA_URL, json={
            "model": MODELO_LOCAL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "format": "json"
        }, timeout=60.0)
        
        if response.status_code == 200:
            return json.loads(response.json().get("message", {}).get("content", "{}"))
    except Exception as e:
        print(f"Erro ao processar {nome_arquivo} com IA: {e}")
    return {"categoria": "Não Identificado", "tags": [], "resumo_executivo": "Falha ao extrair resumo."}

def executar_mapeamento():
    print("🔍 Iniciando varredura no Catunda_SSD...")
    
    # Forçamos uma inicialização limpa em formato de Dicionário para evitar conflitos com listas vazias
    mapa_completo = {"arquivos": {}}

    if not os.path.exists(RAIZ_SEGURA):
        print(f"Erro: A pasta {RAIZ_SEGURA} não existe.")
        return

    arquivos = [f for f in os.listdir(RAIZ_SEGURA) if os.path.isfile(os.path.join(RAIZ_SEGURA, f)) and not f.startswith('.')]

    for arquivo in arquivos:
        if arquivo == "mapa_conhecimento.json":
            continue
            
        caminho_completo = os.path.join(RAIZ_SEGURA, arquivo)
        mtime = os.path.getmtime(caminho_completo)
        data_modificacao = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
        
        print(f"-> Processando: {arquivo}")
        
        try:
            with open(caminho_completo, 'r', encoding='utf-8', errors='ignore') as f:
                conteudo = f.read(2048)
                
            metadados_ia = extrair_metadados_com_ia(arquivo, conteudo)
            
            # Garante a inserção indexada por nome de arquivo
            mapa_completo["arquivos"][arquivo] = {
                "categoria": metadados_ia.get("categoria", "Geral"),
                "tags": metadados_ia.get("tags", []),
                "resumo_executivo": metadados_ia.get("resumo_executivo", ""),
                "ultima_modificacao": data_modificacao
            }
        except Exception as e:
            print(f"Erro ao ler arquivo {arquivo}: {e}")

    # Salva o resultado final estruturado sobrepondo o arquivo antigo corrompido
    with open(MAPA_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(mapa_completo, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Mapeamento concluído! O arquivo {MAPA_JSON_PATH} foi atualizado com sucesso.")

if __name__ == "__main__":
    executar_mapeamento()