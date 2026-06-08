---
tipo: project
titulo: Canal de Ferramentas de IA / Dev Productivity (afiliados)
criado: 2026-06-07
atualizado: 2026-06-07
tags: [agentic-workflows, monetizacao, projeto, ferramentas]
status: ideia
objetivo: "Monetizar via afiliados de ferramentas de IA/dev, usando o próprio wiki como motor de conteúdo e short-form como topo de funil."
ferramentas: [n8n, letta, qmd]
fontes: []
---

# Projeto — Canal de Ferramentas de IA / Dev Productivity

> Primeiro projeto do vault. Nasce do cruzamento das áreas [[agentic-workflows-monetizacao]] + [[memoria-permanente-llm-landscape-2026|memória permanente]].

## Tese do projeto
Eu **já avalio ferramentas de IA** e arquivo cada uma como página `tool` com veredito honesto. Esse trabalho vira **conteúdo** quase de graça. Monetização por **afiliados** das ferramentas que eu genuinamente uso — alinhamento natural entre o que reviso e o que recomendo.

**O moat:** o [[padrao-llm-wiki-conceito|wiki]] é o motor de conteúdo. Cada deep-dive de tool já é o roteiro de um vídeo/post. Ninguém com planilha solta replica isso fácil.

## Funil (revenue stacking — ver [[agentic-workflows-monetizacao-landscape-2026]])
1. **Topo / Short-form** (TikTok, Shorts, Reels): "1 ferramenta, 1 problema resolvido em 60–75s". Loss leader, alcance.
2. **Meio / Long-form** (YouTube, nicho tech = RPM $15–40/1k): deep-dive, comparativo, tutorial. Onde mora a autoridade e o ad revenue eventual.
3. **Conversão / Afiliados**: link da ferramenta na descrição + página/comparativo no blog. Receita primária.

## Pipeline agêntico (híbrido, human-in-the-loop OBRIGATÓRIO)
> YouTube (jul/2025) desmonetiza conteúdo 100% IA. Revisão humana não é opcional.

```
[wiki tool page]  →  roteiro (LLM)  →  [VOCÊ aprova/edita]  →  voz+visual  →  agendamento ([[n8n]])  →  publicação
                                                                                      ↓
                                                          analytics → memória do agente ([[letta]]) → ajusta próximo tema
```

- **n8n** ([[n8n]]): orquestração determinística (agendamento, multi-plataforma, publicação).
- **letta** ([[letta]]): camada de memória/estratégia — lembra o que performou e ajusta o mix de temas.
- **qmd** ([[qmd]]): busca no próprio wiki para achar o próximo tool a virar conteúdo.
- **Gate humano**: você aprova roteiro e veredito antes de publicar (compliance + qualidade emocional que o agente não julga).

## Monetização
- **Primária:** afiliados de ferramentas de IA/dev já avaliadas. Pesquisa dos programas → [[programas-afiliado-ferramentas-ia]].
- **Secundária (futuro):** ad revenue long-form quando houver audiência; produto digital (o próprio sistema) como upsell.

### Achado-chave dos afiliados (2026-06-07)
Das tools no vault, **só [[n8n]] tem afiliado** (30%/12m). Memória ([[mem0]]/[[zep]]/[[letta]]…) = conteúdo, não comissão. → **Estratégia de duas trilhas:**
- **Conteúdo (autoridade):** revisar as melhores tools honestamente, com afiliado ou não. Confiança = ativo real.
- **Receita (afiliados):** monetizar onde há programa, priorizando o que você **usa de verdade**.

**Piloto recomendado:**
1. **[[n8n]]** — já no stack, afiliado 30%/12m. Âncora. (⚠️ programa proíbe tráfego pago.)
2. **Speechify** — TTS do próprio pipeline + 50% comissão (uso real + monetização).
3. **[[letta]]** — só conteúdo de autoridade, sem expectativa de afiliado.

## Métricas & ROI honesto (ritual do schema)
- Medir **custo real** (API + tempo seu de aprovação) vs. **receita atribuível** (cliques/conversões de afiliado por vídeo).
- Não declarar "deu certo" sem atribuição honesta — sem cherry-picking de 1 vídeo viral.
- KPIs iniciais: cliques de afiliado / 1k views; conversão; custo por vídeo publicado.

## Riscos
- Políticas anti-IA/anti-automação das plataformas → mitigado pelo gate humano.
- Saturação do nicho "AI tools" → diferenciar pela **profundidade honesta** (veredito com contras, não só hype).
- Conflito de interesse afiliado × honestidade → regra: veredito é escrito **antes** de checar se há programa de afiliado.

## Próximos passos
1. ✅ Pesquisar programas de afiliado → [[programas-afiliado-ferramentas-ia]] (n8n confirmado; Speechify alta sinergia).
2. Confirmar termos no site oficial de n8n e Speechify; aplicar aos programas.
3. Definir 1 plataforma para começar (recomendação: YouTube long-form + Shorts, pelo RPM).
4. Montar o primeiro workflow n8n mínimo (1 vídeo, fim a fim, com gate humano).
5. Rodar 1 vídeo piloto e medir (cliques de afiliado/1k views) antes de escalar.

## Conexões
- Área → [[agentic-workflows-monetizacao]].
- Usa → [[n8n]], [[letta]], [[qmd]].
- Pergunta-mãe → [[agentic-workflows-monetizacao-landscape]].
