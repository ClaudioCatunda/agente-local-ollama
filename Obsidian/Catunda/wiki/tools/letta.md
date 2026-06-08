---
tipo: tool
titulo: Letta (MemGPT)
criado: 2026-06-07
atualizado: 2026-06-07
tags: [memoria, ferramenta, agentes, framework]
fontes: []
categoria: framework
maturidade: estavel
local_first: sim
licenca: Apache-2.0
veredito: "Melhor abstração conceitual (memória como SO); ideal para agentes long-running self-hosted onde o LLM gerencia o que paginar. Bom encaixe com o foco local-first do Catunda."
---

# Letta (MemGPT)

Modela memória do agente como um **sistema operacional**: contexto principal = RAM (rápido, limitado), storage externo = disco (lento, ilimitado), e o **agente decide** quando paginar informação para dentro/fora do contexto.

## Prós
- Abstração elegante e poderosa (LLM-managed memory).
- Self-hostável, Apache-2.0, ~83% LoCoMo.
- Bom para agentes de longa duração.

## Contras / riscos
- É um framework: exige construir o agente em volta dele.
- Paginação gerida por LLM = custo/latência variáveis.

## Conexões
- Compete/complementa [[mem0]], [[zep]], [[superlocalmemory]].
- Ideia "disco ilimitado" combina com um vault markdown como backend → ver pergunta derivada em [[memoria-permanente-llm-landscape-2026]].
