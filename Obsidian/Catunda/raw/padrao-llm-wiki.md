# LLM Wiki (idea file)

> Fonte bruta IMUTÁVEL. Capturada em 2026-06-07. Não editar.
> Origem: idea file fornecido por Catunda (padrão para construir bases de conhecimento pessoais com LLMs).

## A ideia central

A maioria das pessoas usa LLM + documentos como RAG: você sobe arquivos, o LLM recupera chunks relevantes na hora da query e gera resposta. Funciona, mas o LLM redescobre o conhecimento do zero a cada pergunta. Não há acumulação.

A ideia aqui é diferente. Em vez de só recuperar de documentos brutos na query, o LLM constrói e mantém incrementalmente um **wiki persistente** — coleção estruturada e interligada de arquivos markdown entre você e as fontes brutas. Ao adicionar uma fonte, o LLM lê, extrai o essencial e integra ao wiki existente — atualizando páginas de entidade, revisando resumos de tópico, anotando onde dados novos contradizem afirmações antigas. O conhecimento é compilado uma vez e mantido atual, não re-derivado a cada query.

Diferença-chave: o wiki é um artefato persistente e composto. Cross-references já estão lá. Contradições já foram sinalizadas. A síntese já reflete tudo que foi lido. O wiki fica mais rico a cada fonte e a cada pergunta.

Você quase nunca escreve o wiki — o LLM escreve e mantém tudo. Você cuida do sourcing, exploração e das perguntas certas. O LLM faz o trabalho braçal: resumir, cruzar referências, arquivar, bookkeeping. Na prática: LLM de um lado, Obsidian do outro. Obsidian é a IDE; o LLM é o programador; o wiki é o codebase.

## Contextos de aplicação

- Pessoal: metas, saúde, psicologia, autoconhecimento.
- Pesquisa: deep-dive num tema por semanas/meses, tese que evolui.
- Leitura de livro: arquivar cada capítulo, páginas de personagens/temas (tipo fan wikis como Tolkien Gateway).
- Negócio/time: wiki interno alimentado por Slack, transcrições de reunião, docs de projeto, calls de cliente.
- Competitive analysis, due diligence, planejamento de viagem, notas de curso, hobbies.

## Arquitetura — três camadas

1. **Raw sources** — coleção curada de documentos. Imutáveis. Fonte da verdade.
2. **The wiki** — diretório de markdown gerado pelo LLM. Summaries, entity pages, concept pages, overview, síntese. LLM é dono total.
3. **The schema** — documento (CLAUDE.md / AGENTS.md) que diz ao LLM como o wiki é estruturado, convenções e workflows. Configuração-chave que torna o LLM um mantenedor disciplinado.

## Operações

- **Ingest:** solta fonte em raw, manda processar. LLM lê, discute takeaways, escreve summary, atualiza index, atualiza entidades/conceitos, append no log. Uma fonte pode tocar 10–15 páginas. Pode ser 1-por-vez supervisionado ou batch.
- **Query:** pergunta contra o wiki. LLM busca páginas relevantes, lê, sintetiza com citações. Boas respostas podem ser arquivadas como páginas novas (notes), para explorações comporem o wiki.
- **Lint:** health-check periódico. Procura contradições, afirmações obsoletas, páginas órfãs, conceitos sem página, cross-references faltando, lacunas de dados. Sugere novas perguntas e fontes.

## Indexação e log

- **index.md** — orientado a conteúdo. Catálogo de tudo, link + resumo de 1 linha + metadados, por categoria. Atualizado a cada ingest. Funciona bem até escala moderada (~100 fontes, centenas de páginas) sem RAG por embeddings.
- **log.md** — cronológico, append-only. Prefixo consistente (`## [2026-04-02] ingest | Título`) torna parseável: `grep "^## \[" log.md | tail -5`.

## Ferramentas opcionais

- Busca: index basta no início; `qmd` (busca local markdown, BM25/vetorial + re-rank LLM, CLI + MCP server) ou script próprio.
- Obsidian Web Clipper (artigo→markdown), download de imagens local (Attachment folder + hotkey), graph view, Marp (slides), Dataview (queries sobre frontmatter).
- O wiki é só um repo git de markdown — version history, branching, colaboração de graça.

## Por que funciona

A parte tediosa de manter uma base de conhecimento não é ler ou pensar — é o bookkeeping. Humanos abandonam wikis porque a manutenção cresce mais rápido que o valor. LLMs não cansam, não esquecem de atualizar uma cross-reference, tocam 15 arquivos numa passada. A manutenção custa quase zero. Trabalho do humano: curar fontes, direcionar análise, perguntar bem, pensar no significado. Trabalho do LLM: todo o resto.

## Linhagem

Relacionado ao Memex de Vannevar Bush (1945) — store de conhecimento pessoal e curado, com trilhas associativas entre documentos. A parte que ele não resolveu: quem faz a manutenção. O LLM resolve isso.

## Nota

O documento é intencionalmente abstrato — descreve a ideia, não uma implementação específica. Estrutura de diretórios, convenções de schema, formatos de página, tooling: tudo depende do domínio, preferências e LLM escolhido. Tudo é opcional e modular.
