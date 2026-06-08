---
tipo: note
titulo: Memória permanente para LLMs — landscape 2026
criado: 2026-06-07
atualizado: 2026-06-07
tags: [memoria, agentes, pesquisa, landscape]
fontes: []
responde: [memoria-permanente-llm]
---

# Memória permanente para LLMs — landscape 2026

> Nota de pesquisa (query com busca web, 2026-06-07). Responde parcialmente → [[memoria-permanente-llm]].

## Resposta curta
Em 2026 a discussão "vetor vs. grafo" **acabou**: o consenso de produção é **híbrido** — vetor para entrada semântica, grafo/entidades para profundidade relacional, organizado numa **hierarquia de 3 camadas**. Mas há um caminho que os vendors quase ignoram e que é exatamente o deste vault: **memória baseada em arquivos markdown** mantida por LLM ([[padrao-llm-wiki-conceito]]). Ver contraste em [[rag-vs-wiki-persistente]].

## Hierarquia de 3 camadas (consenso 2025–2026)
1. **Working memory (in-context)** — buffer da sessão atual, tool calls, estado ativo.
2. **Session-scoped** — fatos resumidos/extraídos da sessão, sob demanda.
3. **Long-term persistente** — conhecimento cross-sessão, preferências, workflows; em store vetor+grafo.

Taxonomia cognitiva paralela: **episódica** (o que aconteceu), **semântica** (o que se sabe), **procedural** (como fazer).

## Comparativo de frameworks

| Ferramenta | Arquitetura | Local-first | Licença | LoCoMo* | Caso ideal |
|---|---|---|---|---|---|
| [[mem0]] | Híbrido (vetor+grafo+KV), API/open-core | ❌ não | Open core | ~58–66% | Personalização, infra gerenciada |
| [[zep]] | Knowledge graph temporal | ✅ Community Ed. | Apache-2.0 + comercial | ~85% | Raciocínio temporal, produção em escala |
| [[letta]] | "OS de memória" (MemGPT), LLM pagina contexto | ✅ framework | Apache-2.0 | ~83% | Agentes long-running, lógica de memória customizada |
| [[superlocalmemory]] | Local-first, 3 camadas matemáticas | ✅ (foco) | MIT | até ~87,7% | Privacidade, zero-cloud, compliance (EU AI Act) |

\* *Benchmark LoCoMo — números variam muito por fonte e por self-report. Tratar como ordem de grandeza, não verdade absoluta. Ver "Hype vs. comprovado".*

## Benchmarks citados
- **LoCoMo** e **LongMemEval** — conversas longas / memória de longo prazo.
- **BEAM** — contexto de 1M→10M tokens; queda de ~25% (64,1 → 48,6) revela o gargalo de **abstração temporal em escala**.
- ⚠️ **Hype vs. comprovado:** a Mem0 reporta no próprio blog LongMemEval **94,4** e LoCoMo **92,5**; comparativos independentes colocam a Mem0 em **~49–66%** no LoCoMo. Self-report de vendor ≠ benchmark neutro. Não reportar número sem citar a metodologia. (Ritual do schema, seção 0.5.)

## Problemas em aberto (não resolvidos em 2026)
- Abstração temporal em escala (queda 1M→10M tokens).
- Resolução de identidade cross-sessão/cross-device.
- Staleness de fatos de alta relevância.
- Tratar mudança como **evolução**, não substituição (exatamente o que o wiki faz com `> ⚠️ Contradição`).
- Arquitetura de privacidade/consentimento.

## Conexão com este vault
Os frameworks acima resolvem memória **para agentes em runtime** (extração automática, retrieval). O [[padrao-llm-wiki-conceito|padrão LLM Wiki]] resolve um problema vizinho mas distinto: memória **legível por humano, curada, que compõe** — onde o LLM faz o bookkeeping. São complementares: um wiki markdown poderia ser a camada *long-term* legível, e uma ferramenta como [[letta]]/[[zep]] a camada de retrieval automático. Boa pergunta derivada ↓.

## Perguntas derivadas (candidatas a abrir)
- Dá para usar um vault markdown (este) como backend de long-term memory de um agente Letta/Mem0?
- Qual o melhor local-first puro para um Mac Mini Apple Silicon (sem cloud)?

## Fontes
- [State of AI Agent Memory 2026 — Mem0](https://mem0.ai/blog/state-of-ai-agent-memory-2026)
- [5 AI Agent Memory Systems Compared (2026 Benchmark) — dev.to](https://dev.to/varun_pratapbhardwaj_b13/5-ai-agent-memory-systems-compared-mem0-zep-letta-supermemory-superlocalmemory-2026-benchmark-59p3)
- [Vector DB vs Knowledge Graph for Agent Memory — Atlan](https://atlan.com/know/vector-database-vs-knowledge-graph-agent-memory/)
- [Best AI Agent Memory Systems in 2026 — Vectorize](https://vectorize.io/articles/best-ai-agent-memory-systems)
