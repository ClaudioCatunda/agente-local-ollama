---
tipo: concept
titulo: Padrão LLM Wiki
criado: 2026-06-07
atualizado: 2026-06-07
tags: [knowledge-management, metodo, llm]
fontes: [padrao-llm-wiki]
---

# Padrão LLM Wiki

Padrão em que um **LLM constrói e mantém incrementalmente um wiki persistente** de markdown interligado, posicionado entre o usuário e as fontes brutas. O conhecimento é **compilado uma vez e mantido atual**, não re-derivado a cada query.

## Características
- **Persistente e composto:** cross-references, contradições e síntese já existem; o wiki enriquece a cada fonte/pergunta.
- **Divisão de trabalho:** humano = sourcing + perguntas; LLM = bookkeeping.
- **Analogia:** Obsidian = IDE, LLM = programador, wiki = codebase.

## Relações
- Contrasta com → [[rag-vs-wiki-persistente]].
- Implementado via → [[ingest-query-lint]].
- Antecessor conceitual → [[vannevar-bush]] (Memex).
- Fonte → [[padrao-llm-wiki]].
