---
tipo: tool
titulo: Zep (Graphiti)
criado: 2026-06-07
atualizado: 2026-06-07
tags: [memoria, ferramenta, grafo, temporal]
fontes: []
categoria: memoria
maturidade: maduro
local_first: parcial
licenca: Apache-2.0 + comercial
veredito: "Melhor para raciocínio temporal e produção em escala; Community Edition self-hostável. Forte candidato se o projeto precisa de 'estado que muda no tempo'."
---

# Zep (Graphiti)

Memory server com **knowledge graph temporal**: guarda fatos com timestamps e mapas de relação, entendendo **mudança de estado** (ex.: usuário mudou de Londres → Tóquio; vetor simples retornaria as duas como atuais). Faz summarization e extração de entidade de forma assíncrona — é um servidor completo, não só biblioteca.

## Prós
- Modelagem temporal de ponta (state change).
- ~85% LoCoMo em comparativos independentes (topo da tabela).
- Community Edition self-hostável (Apache-2.0).

## Contras / riscos
- Mais pesado que uma lib (servidor + grafo).
- Local-first **parcial** — full features tendem ao comercial/cloud.

## Conexões
- Compete com [[mem0]], [[letta]], [[superlocalmemory]].
- O tratamento de "mudança como evolução" ecoa o `> ⚠️ Contradição` deste wiki → [[ingest-query-lint]].
- Contexto → [[memoria-permanente-llm-landscape-2026]].
