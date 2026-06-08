---
tipo: question
titulo: Qual a melhor arquitetura de memória permanente para LLMs?
criado: 2026-06-07
atualizado: 2026-06-07
tags: [memoria, agentes, pesquisa]
status: em-investigacao
prioridade: alta
fontes: []
---

# Qual a melhor arquitetura de memória permanente para LLMs?

## Pergunta
Como dar a um agente LLM memória que **compõe** ao longo do tempo, sem re-derivar tudo a cada sessão? Quais abordagens valem a pena hoje?

## Achados (2026-06-07, busca web) → [[memoria-permanente-llm-landscape-2026]]
- Consenso 2026 = **híbrido** (vetor+grafo+entidades) em **hierarquia de 3 camadas**.
- Contendores deep-dived: [[zep]] (temporal, ~85% LoCoMo), [[letta]] (OS de memória, local), [[mem0]] (default, não local-first), [[superlocalmemory]] (local-first/MIT).
- Para o critério **local-first** do Catunda (Mac Mini): [[superlocalmemory]] e [[letta]] na frente.
- ⚠️ Benchmarks self-reported inflam; tratar com ceticismo.

## Eixos a investigar
- Wiki persistente de markdown (este vault / [[padrao-llm-wiki-conceito]]) vs. RAG por embeddings vs. memória estruturada (grafos).
- Memória de arquivo vs. vector DB vs. híbrido.
- Quem mantém a consistência — humano, LLM, ou tooling automático.

## Próximos passos
- Testar [[superlocalmemory]] e [[letta]] no Mac Mini.
- Investigar pergunta derivada: vault markdown como backend long-term de um agente.

## Estado
**Em investigação.** Achados parciais documentados. Relacionada à tese central → [[overview]].
