---
tipo: concept
titulo: RAG vs. Wiki Persistente
criado: 2026-06-07
atualizado: 2026-06-07
tags: [rag, knowledge-management, llm]
fontes: [padrao-llm-wiki]
---

# RAG vs. Wiki Persistente

| Aspecto | RAG clássico | Wiki persistente (este vault) |
|---|---|---|
| Quando o conhecimento é processado | Na hora da query | Uma vez, no ingest; mantido atual |
| Acumulação | Nenhuma — redescobre do zero | Compõe a cada fonte/pergunta |
| Cross-references | Inexistentes | Já presentes |
| Contradições | Não detectadas | Sinalizadas no ingest |
| Síntese multi-documento | Refeita toda query | Já reflete tudo lido |
| Infra | Embeddings/vector DB | `index.md` + `log.md` (até ~100 fontes) |

## Por quê
Re-derivar a cada query é caro e não compõe. Compilar uma vez e manter atual transfere o custo para o ingest (barato com LLM) e entrega respostas mais ricas.

## Relações
- Faz parte de → [[padrao-llm-wiki-conceito]].
- Fonte → [[padrao-llm-wiki]].
