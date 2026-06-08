---
tipo: tool
titulo: qmd
criado: 2026-06-07
atualizado: 2026-06-07
tags: [busca, ferramenta, local-first, software]
fontes: [padrao-llm-wiki]
categoria: busca
maturidade: estavel
local_first: sim
licenca: open-source
veredito: "Busca local on-device sobre markdown (BM25+vetorial+re-rank LLM); candidata natural quando este wiki passar de ~100 fontes. Hoje o index.md basta."
---

# qmd

Motor de busca local sobre arquivos markdown, com busca híbrida **BM25 + vetorial** e re-ranking por LLM, tudo on-device. Tem CLI (LLM pode fazer shell out) e MCP server (uso como ferramenta nativa).

## Quando usar
Opcional. No início, o [[index|index.md]] basta. Conforme o wiki crescer (~100 fontes), considerar `qmd` para busca apropriada.

## Conexões
- Tooling opcional do → [[padrao-llm-wiki-conceito]].
- Candidata da question [[landscape-ferramentas-agentes]] (falta deep-dive real).
- Fonte → [[padrao-llm-wiki]].
