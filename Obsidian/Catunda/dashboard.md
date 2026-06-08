---
tipo: overview
titulo: Dashboard (Dataview)
atualizado: 2026-06-07
---

# 📊 Dashboard

> Tabelas geradas automaticamente a partir do frontmatter (Dataview). Atualizam sozinhas a cada página nova. Para navegação textual canônica, ver também [[index]].

## 🛠️ Ferramentas
```dataview
TABLE categoria AS "Categoria", maturidade AS "Maturidade", local_first AS "Local-first", veredito AS "Veredito"
FROM "wiki/tools"
WHERE tipo = "tool"
SORT local_first DESC, titulo ASC
```

## ❓ Perguntas de pesquisa
```dataview
TABLE prioridade AS "Prioridade", status AS "Status"
FROM "wiki/questions"
WHERE tipo = "question"
SORT prioridade ASC, status ASC
```

## 🚀 Projetos
```dataview
TABLE status AS "Status", objetivo AS "Objetivo"
FROM "wiki/projects"
WHERE tipo = "project"
SORT status ASC
```

## 📥 Fontes ingeridas
```dataview
TABLE ingerido AS "Ingerido", fonte_url AS "URL"
FROM "wiki/sources"
WHERE tipo = "source"
SORT ingerido DESC
```

## 📝 Notas / Explorações
```dataview
TABLE atualizado AS "Atualizado", join(tags, ", ") AS "Tags"
FROM "wiki/notes"
WHERE tipo = "note"
SORT atualizado DESC
```

## 🧩 Conceitos & Entidades
```dataview
LIST
FROM "wiki/concepts" OR "wiki/entities"
SORT file.name ASC
```
