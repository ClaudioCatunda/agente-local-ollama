---
tipo: concept
titulo: Ingest, Query, Lint
criado: 2026-06-07
atualizado: 2026-06-07
tags: [workflow, metodo]
fontes: [padrao-llm-wiki]
---

# Ingest · Query · Lint

As três operações centrais do wiki. Detalhe operacional no schema (`CLAUDE.md`).

## Ingest
Catunda solta fonte em `raw/` → eu leio, discuto takeaways, escrevo `wiki/sources/<slug>`, atualizo entidades/conceitos, sinalizo contradições, atualizo `overview` e `index`, append no `log`. Uma fonte pode tocar 10–15 páginas. Padrão: 1-por-vez, supervisionado.

## Query
Pergunta contra o wiki → leio `index` primeiro, aprofundo, sintetizo **com citações**. Respostas valiosas são arquivadas em `wiki/notes/` para comporem o wiki.

## Lint
Health-check: contradições, afirmações obsoletas, páginas órfãs, conceitos sem página, cross-refs faltando, lacunas de dados. Saída: lista priorizada + novas perguntas/fontes sugeridas.

## Relações
- Operacionaliza → [[padrao-llm-wiki-conceito]].
- Fonte → [[padrao-llm-wiki]].
