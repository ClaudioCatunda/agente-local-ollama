# 🎯 Plano de Estudos e Memória de Atividades - IA 2026

## 📌 Escopo do Projeto e Diretrizes Nacionais
* **Ambiente de Execução:** Mac mini M4, 26GB RAM, ambiente isolado em `.venv` apontando para a pasta `Developer` no `Catunda_SSD`.
* **Modelos Utilizados:** `llama3.2:latest` (Síntese e Classificação) e `nomic-embed-text:latest` (Vetorização Matemática).
* **Stack Tecnológica:** Python 3, HTTPX, ChromaDB (Embedded), Git.

---

## 🪵 Histórico de Atividades Realizadas

### 1. Diagnóstico de Infraestrutura e Timeout
* **Incidente:** O modelo local de 3B apresentou falhas de *timeout* (tempo limite de 30s estourado via HTTPX) ao tentar processar arquivos Markdown de infraestrutura (16KB+).
* **Solução:** Implementação de Engenharia de Contexto via Python, limitando a leitura física do SSD para blocos máximos de 4KB por arquivo e expansão do timeout do payload para 90 segundos.

### 2. Transição para Arquitetura Determinística (Baseada em Regras)
* **Mudança Estratégica:** Substituição do loop de tomada de decisão autônoma (*ReAct/JSON*), que causava degradação cognitiva e alucinação de nomes de arquivos, por um fluxo orquestrado pelo Python.
* **Mecânica:** O Python varre o hardware diretamente, passa as opções reais ao Llama para classificação estrita e o modelo devolve apenas a síntese final com base em dados injetados.

### 3. Fase 1: Criação do Indexador de Metadados
* **Script:** `mapeador_contexto.py`
* **Resultado:** Varredura automática do diretório e geração estruturada do `mapa_conhecimento.json`. Os arquivos são indexados por categorias, tags e resumos executivos.

### 4. Fase 2: Implementação de Memória por Janela Deslizante
* **Mecânica:** Algoritmo implementado no loop principal do chat que preserva o *System Prompt* intacto e retém apenas as últimas 4 mensagens da sessão. Evita sobrecarga de contexto e lentidão no Ollama.

### 5. Fase 3: Integração do Motor RAG Local e Streaming
* **Script:** `indexador_vetorial.py`
* **Mecânica:** Fatiamento dos arquivos em pedaços de 1.000 caracteres, geração de vetores através do `nomic-embed-text` e persistência no banco vetorial **ChromaDB** no SSD.
* **Otimização:** Ativação de `stream: True` via `httpx.stream` no `agente_local.py`, tornando as respostas do chat instantâneas no terminal.

---

## 🚀 Próximos Marcos de Evolução (Roadmap)

* [ ] **Meta 1 (Ingestão Avançada):** Adaptar o `indexador_vetorial.py` com bibliotecas de extração para suportar leitura de PDFs técnicos e planilhas.
* [ ] **Meta 2 (Reranking):** Implementar um modelo local leve de classificação de relevância para refinar os fragmentos trazidos pelo ChromaDB antes de passá-los ao Llama.
* [ ] **Meta 3 (Pipeline Automatizado):** Integrar a biblioteca `watchdog` no Python para atualizar o banco vetorial e o arquivo JSON em segundo plano de forma automática sempre que um documento no SSD for alterado.