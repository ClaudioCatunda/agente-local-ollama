import os
import httpx
import json
import chromadb

# Configurações de Caminhos no Catunda_SSD
RAIZ_SEGURA = "/Volumes/Catunda_SSD/Developer/Documents"
CHROMA_PATH = "/Volumes/Catunda_SSD/Developer/chroma_db"

# Configurações do Ollama
OLLAMA_EMBED_URL = "http://localhost:11434/api/embeddings"
MODELO_EMBED = "nomic-embed-text:latest"

def obter_embedding_ollama(texto: str) -> list:
    """Chama o modelo matemático local para gerar o vetor do fragmento de texto."""
    try:
        response = httpx.post(OLLAMA_EMBED_URL, json={
            "model": MODELO_EMBED,
            "prompt": texto
        }, timeout=30.0)
        
        if response.status_code == 200:
            return response.json().get("embedding")
        else:
            print(f"❌ Erro na API do Ollama: {response.status_code}")
    except Exception as e:
        print(f"❌ Falha de conexão ao gerar embedding: {e}")
    return []

def fatiar_texto(texto: str, tamanho_chunk: int = 1000, overlap: int = 200) -> list:
    """Corta o texto em blocos menores com uma zona de sobreposição (overlap) para não perder contexto."""
    chunks = []
    inicio = 0
    while inicio < len(texto):
        fim = inicio + tamanho_chunk
        chunks.append(texto[inicio:fim])
        inicio += (tamanho_chunk - overlap)
    return chunks

def executar_indexacao():
    print("📦 Inicializando Banco Vetorial ChromaDB no SSD...")
    # Cria o cliente persistente apontando para o Catunda_SSD
    cliente_chroma = chromadb.PersistentClient(path=CHROMA_PATH)
    
    # Cria ou obtém a coleção de vetores
    colecao = cliente_chroma.get_or_create_collection(name="documentos_developer")
    
    # Varre a pasta Documents
    arquivos = [f for f in os.listdir(RAIZ_SEGURA) if os.path.isfile(os.path.join(RAIZ_SEGURA, f)) and f.endswith(('.md', '.txt'))]
    
    if not arquivos:
        print("⚠️ Nenhum arquivo de texto válido encontrado para indexação.")
        return

    for arquivo in arquivos:
        # Pula arquivos de controle interno
        if arquivo in ["mapa_conhecimento.json", "INDICE_GERAL.md"]:
            continue
            
        caminho_completo = os.path.join(RAIZ_SEGURA, arquivo)
        print(f"📂 Fatiando e vetorizando: {arquivo}...")
        
        try:
            with open(caminho_completo, 'r', encoding='utf-8', errors='ignore') as f:
                conteudo_completo = f.read()
            
            # Corta o arquivo em pedaços de 1000 caracteres
            fragmentos = fatiar_texto(conteudo_completo)
            
            for idx, fragmento in enumerate(fragmentos):
                # Ignora fragmentos vazios ou irrelevantes
                if not fragmento.strip():
                    continue
                    
                # Identificador único para cada bloco de texto
                doc_id = f"{arquivo}_chunk_{idx}"
                
                # Gera o vetor numérico do pedaço de texto
                vetor = obter_embedding_ollama(fragmento)
                
                if vetor:
                    # Salva no ChromaDB: ID, Vetor, Metadados e o Texto Original
                    colecao.upsert(
                        ids=[doc_id],
                        embeddings=[vetor],
                        metadatas=[{"fonte": arquivo, "chunk": idx}],
                        documents=[fragmento]
                    )
                    
            print(f"   ✅ {len(fragmentos)} fragmentos salvos com sucesso.")
            
        except Exception as e:
            print(f"❌ Erro ao processar o arquivo {arquivo}: {e}")

    print(f"\n🚀 Sucesso! Banco vetorial atualizado localmente em: {CHROMA_PATH}")

if __name__ == "__main__":
    executar_indexacao()