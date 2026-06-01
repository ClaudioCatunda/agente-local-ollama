# CLAUDE.md

## Sobre o usuário

Meu nome é Catunda.

Sou um profissional de tecnologia que utiliza IA como parceira de desenvolvimento para aumentar produtividade, qualidade e velocidade de entrega.

Prefiro soluções robustas, simples de manter e escaláveis.

---

# Ambiente de Desenvolvimento

## Hardware

- Mac Mini Apple Silicon

## Workspace Principal

/Volumes/Catunda_SSD/Developer

**Regra obrigatória:** Todo e qualquer arquivo, projeto ou alteração deve ser criado e mantido exclusivamente dentro de `/Volumes/Catunda_SSD/Developer`. Nunca criar arquivos no armazenamento interno do Mac Mini (`/Users/`, `/home/`, `~/` ou qualquer path fora do SSD). Isso garante separação total entre o ambiente de trabalho e o sistema.

## Ferramentas

- Node.js 26+
- npm 11+
- Git
- Claude Code

---

# Modo de Trabalho

Antes de realizar qualquer alteração:

1. Entenda o objetivo solicitado.
2. Analise o impacto da mudança.
3. Identifique os arquivos envolvidos.
4. Explique resumidamente o plano.
5. Execute a alteração.
6. Informe quais arquivos foram modificados.
7. Informe como validar o resultado.

---

# Regras de Desenvolvimento

## Prioridades

Prioridade máxima:

1. Segurança
2. Estabilidade
3. Legibilidade
4. Manutenção
5. Performance

Nunca sacrificar estabilidade por otimizações prematuras.

---

## Arquitetura

Antes de criar algo novo:

- Procure soluções já existentes no projeto.
- Reutilize componentes sempre que possível.
- Evite duplicação de código.
- Respeite os padrões já adotados.
- Mantenha consistência arquitetural.

---

## Refatoração

Não realizar refatorações extensas sem autorização explícita.

Evitar:

- Mudanças desnecessárias.
- Renomeações massivas.
- Alterações cosméticas sem benefício real.

---

## Dependências

Antes de adicionar uma nova biblioteca:

- Justifique a necessidade.
- Verifique se já existe solução interna.
- Avalie impacto de manutenção.
- Informe vantagens e riscos.

---

# Git

## Workflow obrigatório

Toda nova funcionalidade ou correção deve seguir o fluxo abaixo. **Nunca commitar direto na `main`.**

1. Criar branch a partir da `main`:
   - `feat/<descricao-curta>` para novas funcionalidades
   - `fix/<descricao-curta>` para correções de bugs
   - `refactor/<descricao-curta>` para refatorações
   - `docs/<descricao-curta>` para documentação
2. Implementar e commitar na branch.
3. Abrir Pull Request da branch para `main`.
4. Merge via PR — nunca direto.

## Comandos que nunca executar automaticamente

- git commit
- git push
- git merge
- git rebase

## Sempre apresentar antes de commitar

- arquivos modificados
- resumo das alterações
- sugestão de mensagem de commit

---

# Comunicação

Prefiro respostas:

- objetivas
- técnicas
- diretas

Evitar:

- explicações excessivamente longas
- repetições
- informações irrelevantes

Quando houver múltiplas soluções:

Apresentar:

- vantagens
- desvantagens
- recomendação

---

# Análise de Código

Ao revisar código:

Verificar:

- bugs potenciais
- problemas de segurança
- gargalos de performance
- complexidade desnecessária
- oportunidades de simplificação

Apresentar riscos encontrados por ordem de severidade.

---

# Geração de Código

Código gerado deve:

- ser pronto para produção
- possuir tratamento de erros adequado
- seguir boas práticas da linguagem
- conter comentários apenas quando agregarem valor
- evitar código experimental

---

# Resolução de Problemas

Ao investigar erros:

1. Identifique a causa raiz.
2. Não trate apenas os sintomas.
3. Explique o motivo do problema.
4. Proponha a solução mais simples possível.
5. Apresente alternativas quando relevante.

---

# Tomada de Decisão

Quando existirem várias alternativas:

Avaliar:

- curto prazo
- médio prazo
- longo prazo
- custo de manutenção
- facilidade de evolução

Priorizar soluções sustentáveis.

---

# Segurança

Sempre observar:

- exposição de credenciais
- variáveis de ambiente
- permissões excessivas
- validação de entrada
- riscos de injeção
- dependências vulneráveis

---

# Statistical Analysis / Backtesting

For backtesting and ROI claims, always validate with honest walk-forward methodology to avoid look-ahead bias before reporting results.

---

# Environment / Tooling Notes

Interactive TUI commands (`claude doctor`, `gh auth login`, `npm update` with prompts) cannot be captured via Bash redirection — instruct the user to run them directly rather than attempting to pipe output.

---

# Regra Final

Se houver dúvida sobre uma alteração:

Pare e pergunte antes de modificar.