---
tipo: source
titulo: LLM Wiki (idea file)
criado: 2026-06-07
atualizado: 2026-06-07
tags: [meta, knowledge-management, llm, metodo]
fontes: [padrao-llm-wiki]
fonte_original: raw/padrao-llm-wiki.md
fonte_url: ""
ingerido: 2026-06-07
---

# Resumo — LLM Wiki (idea file)

## TL;DR
Padrão para construir bases de conhecimento pessoais onde o **LLM constrói e mantém incrementalmente um wiki persistente** de markdown interligado, em vez de re-derivar conhecimento do zero a cada query (RAG). O wiki é um artefato que **compõe** com o tempo. Ver [[padrao-llm-wiki-conceito]].

## Pontos-chave
- **RAG vs. wiki persistente:** RAG recupera chunks na hora; o wiki compila o conhecimento uma vez e o mantém atual. Detalhe em [[rag-vs-wiki-persistente]].
- **Divisão de trabalho:** humano faz sourcing, exploração e boas perguntas; LLM faz todo o bookkeeping (resumir, cruzar refs, arquivar). "Obsidian é a IDE; o LLM é o programador; o wiki é o codebase."
- **Três camadas:** `raw/` (fontes imutáveis), `wiki/` (gerado pelo LLM), schema (`CLAUDE.md`).
- **Três operações:** ver [[ingest-query-lint]].
- **Index + log** substituem RAG por embeddings até ~100 fontes.
- **Linhagem:** Memex de [[vannevar-bush]] (1945) — faltava resolver quem mantém; o LLM resolve.

## Ferramentas citadas
- [[obsidian]] como IDE (Web Clipper, graph view, Marp, Dataview).
- [[qmd]] como motor de busca opcional quando escalar.
- Git: o wiki é só um repo de markdown.

## Por que funciona
O gargalo de um knowledge base é o **bookkeeping**, não o pensar. LLMs não cansam e tocam 15 arquivos numa passada → manutenção custa ~zero. É isso que evita o abandono típico de wikis humanos.

## Conexões
- Define o método deste vault inteiro → [[overview]].
- Operacionalizado pelo schema em `CLAUDE.md`.
