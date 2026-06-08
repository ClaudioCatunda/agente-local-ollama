# Log do Wiki

Histórico cronológico append-only. Prefixo consistente para parsing: `grep "^## \[" log.md | tail -5`.

## [2026-06-07] setup | Inicialização do wiki
- Criada estrutura: `raw/`, `raw/assets/`, `wiki/{sources,entities,concepts,notes}`.
- Criados: `CLAUDE.md` (schema), `index.md`, `log.md`.
- Removida nota padrão `Bem-vindo.md`.

## [2026-06-07] ingest | LLM Wiki (idea file)
- fonte: `raw/padrao-llm-wiki.md`
- páginas tocadas: `wiki/sources/padrao-llm-wiki`, `wiki/overview`, `wiki/concepts/padrao-llm-wiki-conceito`, `wiki/concepts/rag-vs-wiki-persistente`, `wiki/concepts/ingest-query-lint`, `wiki/entities/obsidian`, `wiki/entities/vannevar-bush`, `wiki/entities/qmd`, `index`.
- takeaways: o wiki é artefato persistente e composto; LLM faz o bookkeeping; humano faz sourcing/perguntas; 3 camadas (raw/wiki/schema); 3 operações (ingest/query/lint).

## [2026-06-07] setup | Foco definido: pesquisa / deep-dive de IA
- domínio: ferramentas de IA, memória permanente, novos projetos.
- schema: adicionada seção 0.5 (domínio/rituais), tipos `tool`/`project`/`question` no frontmatter, pastas `wiki/{tools,projects,questions}`.
- semeadas 2 perguntas de pesquisa: `memoria-permanente-llm` (alta), `landscape-ferramentas-agentes` (média).
- atualizados `overview`, `index`.

## [2026-06-07] query | Memória permanente para LLMs (busca web)
- pergunta: [[memoria-permanente-llm]] → status aberta ➜ em-investigacao.
- páginas criadas: nota `memoria-permanente-llm-landscape-2026`; tools `mem0`, `zep`, `letta`, `superlocalmemory`.
- páginas tocadas: `questions/memoria-permanente-llm`, `overview`, `index`.
- achados: consenso 2026 = híbrido vetor+grafo em 3 camadas; local-first p/ Mac Mini → superlocalmemory/letta; ⚠️ benchmarks self-reported inflam.
- fontes: mem0.ai/blog, dev.to (5 systems compared), atlan, vectorize.

## [2026-06-07] setup | Nova área: Agentic Workflows para monetização em redes sociais
- schema: adicionado foco #4 na seção 0.5 (com rigor de ROI), tag padrão `agentic-workflows`.
- páginas criadas: hub `concepts/agentic-workflows-monetizacao`; question `agentic-workflows-monetizacao-landscape` (alta).
- páginas tocadas: `overview`, `index`.

## [2026-06-07] query | Agentic workflows p/ monetização (busca web)
- pergunta: [[agentic-workflows-monetizacao-landscape]] → aberta ➜ em-investigacao.
- páginas criadas: nota `agentic-workflows-monetizacao-landscape-2026`; tool `n8n`.
- páginas tocadas: hub `agentic-workflows-monetizacao`, `questions/...`, `overview`, `index`.
- achados: human+IA híbrido obrigatório (YouTube jul/2025); revenue stacking > RPM de Shorts; automação (n8n) vs agente de memória (letta); ⚠️ números de receita majoritariamente self-reported; estudo de caso 6 sem sem ROI comprovado.
- fontes: dev.to (6-week case), mixcord (faceless), browseract (n8n), mirra (ROI plataformas).

## [2026-06-07] lint | Primeiro health-check
- resultado: 0 órfãos, 0 contradições não-tratadas, counts do overview OK.
- corrigido: link fantasma `[[CLAUDE.md]]` → texto; [[qmd]] reclassificado entity→tool; questions `landscape-ferramentas-agentes` aberta➜em-investigacao.
- pendente (decisão do Catunda): páginas de conceito human-in-the-loop / revenue-stacking / hierarquia-memoria-3-camadas; deep-dive real de qmd; definir nicho alto-RPM.

## [2026-06-07] project | Canal de Ferramentas de IA (afiliados)
- decisões: nicho = ferramentas de IA/dev productivity; monetização = afiliados.
- criado: `projects/canal-ferramentas-ia` (status: ideia), usa n8n/letta/qmd.
- páginas tocadas: hub `agentic-workflows-monetizacao`, question `...-landscape`, `overview`, `index`.
- tese: wiki como motor de conteúdo; funil short→long→afiliado; pipeline híbrido com gate humano obrigatório.

## [2026-06-07] query | Programas de afiliado das tools (busca web)
- nota criada: `notes/programas-afiliado-ferramentas-ia`.
- páginas tocadas: `projects/canal-ferramentas-ia`, `overview`, `index`.
- achados: só [[n8n]] tem afiliado (30%/12m, proíbe tráfego pago); memória sem programa; Speechify 50% (sinergia TTS); estratégia de duas trilhas (conteúdo vs receita).
- ⚠️ comissões de agregadores — confirmar no site oficial.
- fontes: n8n.io/affiliates, rewardful, outlierkit.

## [2026-06-07] setup | Obsidian: Dataview + Slides + Web Clipper
- instalados pelo Catunda: Dataview, Slides (core), Web Clipper (navegador).
- criado `dashboard.md` com tabelas Dataview (tools/questions/projects/sources/notes) geradas do frontmatter.
- schema: documentada distinção index.md (canônico p/ LLM) vs dashboard.md (Dataview p/ humano).
