---
tipo: tool
titulo: Mem0
criado: 2026-06-07
atualizado: 2026-06-07
tags: [memoria, ferramenta, agentes]
fontes: []
categoria: memoria
maturidade: estavel
local_first: nao
licenca: open-core
veredito: "Default de mercado para memória de agente; ótimo para personalização gerenciada, mas não é local-first e os benchmarks self-reported inflam o desempenho real."
---

# Mem0

Camada de memória semântica mais deployada em 2026 (~48k★, $24M em out/2025). Pipeline LLM extrai entidades/relações das conversas, guarda como nós+arestas em grafo, cross-linkado a embeddings vetoriais. Três escopos: user, session, agent. Store híbrido vetor+grafo+key-value.

## Prós
- Default geral, maior comunidade, integra com ~21 frameworks e ~20 vector stores.
- Extração automática de memória.

## Contras / riscos
- **Não é local-first** (API/cloud) — choca com o critério `local_first` do Catunda num Mac Mini.
- **Benchmarks self-reported** (LongMemEval 94,4 no próprio blog) divergem de comparativos independentes (~49–66% LoCoMo). Ver ⚠️ em [[memoria-permanente-llm-landscape-2026]].

## Conexões
- Compete com [[zep]], [[letta]], [[superlocalmemory]].
- Contexto → [[memoria-permanente-llm-landscape-2026]] · responde [[memoria-permanente-llm]].
