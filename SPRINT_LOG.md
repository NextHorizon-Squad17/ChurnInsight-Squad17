

# 📜 SPRINT LOG & ARCHITECTURAL JOURNEY | SQUAD 17

> **Documento Vivo:** Este log registra a evolução estratégica, técnica e cultural do projeto **ChurnInsight**. Aqui documentamos não apenas o código, mas as decisões de arquitetura e governança tomadas pela liderança e pelo time.

---
## 🗓️ SPRINT 03: Relatório de Planejamento
**Data:** 22 de Dezembro de 2025 | 
**Status:** Concluído

**Facilitador:** Philipe Oliveira

**Participantes:** Raiuri, Lucas e Felipe (Backend), Romulo (Frontend), Stephanie e Vlademir (Data Science)

---

## 1.0 Resumo Executivo: Alinhamento Estratégico

A Sprint 03 representa um ponto de inflexão crítico para o projeto ChurnInsight. O trabalho planejado para este ciclo transcende a simples implementação de funcionalidades isoladas; seu foco é a validação da arquitetura completa e a mitigação proativa de riscos técnicos complexos. O objetivo é consolidar os componentes desenvolvidos até agora em uma solução coesa, garantindo uma entrega de valor tangível e demonstrável.

O Objetivo Primário da Sprint é: Transformar o protótipo de alta fidelidade em um Release Candidate totalmente funcional, mitigando os riscos da integração End-to-End e validando a confiabilidade da solução para a banca avaliadora do Hackathon.

Para alcançar este resultado, a estratégia da Sprint 03 se apoia em três pilares fundamentais:

* De-risking Técnico: A integração completa entre as frentes de Frontend, Backend e Inteligência Artificial validará a principal cadeia de dependência do projeto e servirá como a prova de conceito final da arquitetura. Este passo é essencial para eliminar incertezas de comunicação entre os sistemas antes da fase de refinamento e otimização, garantindo que a base tecnológica é sólida e escalável.
* Entrega de Valor: Ao final desta Sprint, teremos a primeira versão do produto que demonstra o fluxo de valor completo. Um usuário poderá interagir com a interface, acionar a lógica de negócio no backend, consumir a predição do modelo de IA e receber o resultado em tela, validando a hipótese central do ChurnInsight.
* Maturidade de Governança: A execução bem-sucedida desta integração complexa servirá como um ativo de governança, comprovando a capacidade do Squad 17 de planejar, executar e entregar projetos de alta complexidade técnica. Isso demonstra um nível de maturidade operacional que é um diferencial competitivo chave.

A concretização destes objetivos é sustentada por uma arquitetura tecnológica cuidadosamente selecionada para performance, segurança e escalabilidade.

## 2.0 Arquitetura & Stack Tecnológico: A Engenharia da Solução

As escolhas tecnológicas para o ChurnInsight não foram acidentais; elas refletem uma decisão consciente de construir uma solução robusta, performática e em conformidade com os padrões de uma aplicação de nível empresarial. A arquitetura foi desenhada para garantir escalabilidade, segurança de dados e uma experiência de usuário fluida, desde a interface até o núcleo de inteligência artificial.

A seguir, detalhamos os componentes centrais e a justificativa estratégica para cada tecnologia selecionada:

| Componente | Tecnologia & Justificativa Estratégica |
|------------|----------------------------------------|
| **Backend API** | **Java 25:** Escolhido pela robustez, performance e ecossistema maduro, ideal para a lógica de negócio e orquestração de serviços de uma aplicação Enterprise. |
| **Inteligência Artificial** | **Python/XGBoost:** Utilizado para treinar o modelo de predição de churn, garantindo alta acurácia e performance. A arquitetura de microsserviço para o modelo permite escalabilidade independente. |
| **Frontend** | **Vanilla JS:** Selecionado para garantir leveza e máxima performance no client-side, sem a sobrecarga de frameworks complexos, focando na experiência do usuário. |
| **Infraestrutura & Banco de Dados** | **Oracle Cloud Infrastructure (OCI) / ATP:** Plataforma Cloud-Native que oferece segurança, alta disponibilidade e performance para a persistência de dados, alinhada com as melhores práticas de conformidade (LGPD). |

Esta abordagem arquitetônica pode ser sintetizada em dois conceitos principais: AI-First Architecture, onde o modelo de IA é o núcleo da entrega de valor, e não um complemento; e Cloud-Native Compliance, reforçando que a solução já nasce preparada para um ambiente de produção seguro, resiliente e escalável.

Esta arquitetura robusta serve como alicerce para os entregáveis específicos que serão construídos e integrados ao longo desta Sprint.

## 3.0 Backlog da Sprint & Entregáveis: O Escopo do Trabalho

Esta seção detalha o trabalho tático que será executado pela equipe para atingir o objetivo estratégico da Sprint. As tarefas foram refinadas e distribuídas entre as frentes de trabalho para maximizar o paralelismo e acelerar a integração, permitindo que cada especialista se concentre em sua área de domínio enquanto contribui para a meta unificada.

### 3.1 Backend (Liderado por Raiuri)

* Implementação do sistema de autenticação para que um usuário administrador possa criar e gerenciar as contas do time de marketing, garantindo que o acesso à API seja restrito a usuários autorizados da empresa.
* Configuração final do banco de dados e execução das migrations iniciais para estruturar os dados.
* Construção do endpoint que se comunica com o microsserviço de IA (predict) para obter as predições de churn.

### 3.2 Data Science (Vlademir & Stephanie)

* Finalizar e expor o endpoint do modelo XGBoost treinado para consumo pelo Backend.
* Prestar suporte ativo ao time de Backend para garantir a correta integração e interpretação dos resultados do modelo.

### 3.3 Frontend (Liderado por Rômulo)

* Substituição completa dos dados mockados por chamadas reais à API do Backend.
* Implementação do fluxo de ponta a ponta: interação do usuário que resulta em uma predição de churn exibida na tela.
* Definição e aplicação do novo logo do projeto, conforme as opções apresentadas.

### 3.4 Definition of Done (DoD) Global

O critério de aceite que consolida todos os entregáveis desta Sprint é o seguinte:

"O entregável principal da Sprint será considerado concluído quando uma solicitação iniciada no Frontend atravessar o Backend, obter uma predição válida do serviço de IA e retornar à interface do usuário com uma latência total inferior a 200ms, com os dados da transação devidamente persistidos no banco de dados Oracle ATP."

A execução bem-sucedida deste backlog depende da clareza de papéis e da colaboração eficaz entre os membros do squad.

## 4.0 Matriz de Responsabilidades: Dinâmica do Squad

Em uma fase crítica de integração, a clareza de papéis é fundamental para garantir o alinhamento e a eficiência. A matriz a seguir define os focos primários de cada membro do Squad 17 durante a Sprint 03, promovendo autonomia, responsabilidade e uma comunicação direcionada.

| Membro | Foco Principal na Sprint 03 |
|--------|----------------------------|
| **Philipe (Tech Lead)** | Orquestração da integração, facilitação da comunicação entre frentes e criação de documentação de apoio para acelerar o desenvolvimento do Backend. |
| **Raiuri** | Liderança técnica do Backend, refinamento e distribuição das tarefas de desenvolvimento, arquitetura do sistema de autenticação e configuração da integração contínua (CI/CD). |
| **Lucas & Felipe** | Desenvolvimento dos componentes de autenticação e configuração do banco de dados no Backend, com o suporte do líder técnico. |
| **Rômulo** | Liderança técnica do Frontend, garantindo a substituição dos mocks e a integração bem-sucedida com a nova API. |
| **Vlademir & Stephanie** | Liderança técnica de Data Science, garantindo a disponibilidade e o correto funcionamento do modelo de IA para a integração. |

Com papéis claramente definidos, a equipe pode agora focar proativamente nos potenciais obstáculos que podem impactar a entrega.

## 5.0 Gestão de Riscos & Qualidade: Mitigação e QA

A gestão de riscos é um pilar essencial para o sucesso, especialmente em uma Sprint de alta complexidade como esta. A identificação antecipada de potenciais problemas e o planejamento de estratégias de mitigação são cruciais para garantir que a equipe mantenha o foco na entrega de valor e não seja desviada por imprevistos.

| Risco Identificado | Impacto Potencial | Estratégia de Mitigação |
|-------------------|-------------------|------------------------|
| **Atrasos na integração Backend-Frontend** | Bloqueio do objetivo principal da Sprint, impedindo a validação do fluxo de valor. | Prioridade máxima nas tarefas de integração. PH criará documentação de apoio especificamente para acelerar o desenvolvimento do time de Backend (Lucas & Felipe), detalhando as tarefas e alinhando a abordagem técnica, replicando o modelo de sucesso usado com a frente de Data Science. Adicionalmente, Raiuri criará um diagrama visual para ilustrar a comunicação entre Frontend, Backend e o microsserviço de IA, garantindo um entendimento unificado do fluxo de dados em todo o squad. |
| **Ineficiência nas reuniões diárias** | Perda de tempo de desenvolvimento e desmotivação da equipe. | Reuniões serão mais objetivas e focadas estritamente no andamento do projeto, conforme solicitado por Raiuri. Tópicos não-essenciais serão movidos para comunicação assíncrona. |
| **Disrupção pelo feriado de fim de ano** | Redução da capacidade produtiva e risco de não finalizar os entregáveis a tempo. | A Sprint Demo foi proativamente movida de quinta para sexta-feira. Adicionalmente, a equipe estabeleceu uma meta interna de concluir o desenvolvimento principal até quarta-feira, garantindo que o feriado não impacte a entrega e permitindo tempo para testes finais. |

Todos os endpoints e a persistência de dados devem seguir as diretrizes de segurança, com atenção à conformidade com a LGPD, aproveitando a infraestrutura segura da OCI.

Essa abordagem proativa de gestão de riscos e o compromisso com a qualidade não são apenas práticas internas; são mecanismos que garantem a previsibilidade da entrega e protegem o caminho crítico do projeto.

## 6.0 Diferenciais Competitivos: O Fator "Wow"

As práticas operacionais adotadas pelo Squad 17 vão além do gerenciamento de tarefas. Elas representam diferenciais estratégicos que demonstram maturidade, profissionalismo e uma visão de negócio alinhada com as melhores práticas do mercado, fatores que serão percebidos pela banca avaliadora.

* **Mentalidade FinOps e Eficiência de Recursos:** A escolha da OCI e o foco de Raiuri em implementar uma esteira de CI/CD para automatizar o deployment e colocar o serviço em operação rapidamente não são apenas decisões técnicas. Elas demonstram um compromisso com a otimização de custos operacionais (OpEx) e o uso eficiente de recursos em nuvem, alinhado aos princípios de FinOps, sinalizando uma preocupação com a sustentabilidade financeira do projeto a longo prazo.
* **Governança Acelerada e Produtividade:** A iniciativa de Philipe de criar documentação de apoio para os times de Data Science e Backend é uma ferramenta de governança que reduz a ambiguidade, acelera o desenvolvimento e minimiza o retrabalho. Esta prática evidencia uma maturidade de gestão que vai além do esperado em um Hackathon, focando na produtividade, na escalabilidade do time e na qualidade do produto final.


## 🗓️ SPRINT 02: Demo Report & Review
**Data:** 18 de Dezembro de 2025 | 
**Status:** Concluído com Ressalvas

**Facilitador (Remoto):** Philipe Oliveira

**Participantes:** Felipe (Backend), Romulo (Frontend), Stephanie e Vlademir (Data Science)

---


### 📢 Resumo Executivo
A equipe realizou a apresentação da primeira versão funcional da interface e da API simulada. O Frontend entregou uma experiência visual de alto impacto ("Deep Space" theme), e o Backend garantiu o contrato de dados via Mock. O time de Data Science iniciou a análise da matéria-prima (dados).

### 📦 Entregas Realizadas
1.  **Frontend (Romulo):**
    * **Protótipo Funcional:** Interface SPA construída com *Vanilla JS (ES6+)* e *Tailwind CSS*.
    * **UX/UI:** Implementação de Glassmorphism, Dark Mode nativo e velocímetros SVG dinâmicos para medir "Humor do Cliente".
    * **Performance:** Zero dependências de build (No NPM), focando em carregamento instantâneo.
2.  **Backend (Felipe/Lucas/Raiuri):**
    * **API Mock:** Endpoints retornando JSON estruturado conforme DTOs definidos.
    * **Repositório:** Código enviado para a organização GitHub.
3.  **Data Science (Stephanie/Vlademir):**
    * **Data Check:** Validação de acesso aos dados brutos e início do planejamento de EDA (Análise Exploratória).

### ⚠️ Pontos de Atenção & Compliance (Action Items)
1.  **Ocorrência:** O time de Backend reportou uso do **Java 25**, entretanto O Tech Lead Philipe definiu erroneamente na ADR-004 o uso do Java 17 LTS.
    * **Ação Corretiva:** Realizar correção na ADR-004 para **Java 25**.
2.  **Fluxo de Git (Bypass de PR):**
    * **Ocorrência:** Commit direto na `main` devido a erros no IntelliJ.
    * **Ação:** Tech Lead auxiliará na configuração da IDE para garantir o fluxo correto de Pull Requests na próxima task.
3.  **Tech Debt Frontend:**
    * A solução atual é Vanilla JS. A migração para **React/Vite** permanece no backlog para garantir escalabilidade de componentes futuros.

### 🛠️ Inventário de Ferramentas Atualizado (Snapshot 18/12)
*Registro oficial das tecnologias ativas no projeto:*

* **Gestão:** GitHub Projects (Kanban), Google AI Studio (Gemini 3 PRO).
* **Backend:** IntelliJ IDEA, Java 25, Spring Boot, Maven, Postman/Insomnia.
* **Frontend:** VS Code, JavaScript (ES6+), Tailwind CSS (CDN), Live Server.
* **Data Science:** Google Colab, Pandas, NumPy, Scikit-learn, Matplotlib/Seaborn.
* **DevOps/Infra:** Git, GitHub Organizations, Docker (Planejado).

---




## 🗓️ SPRINT 01: Planning & Arquitetura Híbrida
**Data:** 15 de Dezembro de 2025 | **Fase:** Definição Arquitetural & Início do Code

### 🚀 Resumo Executivo
Nesta Planning, elevamos o nível de maturidade do projeto. Para mitigar riscos de integração e garantir o 1º lugar, definimos uma **Estratégia Híbrida de Dados** e uma arquitetura de desenvolvimento desacoplada (**Mock-First**). O objetivo é garantir que Backend e Data Science caminhem em paralelo sem bloqueios.

### 🏛️ Decisões Estratégicas (C-Level)

#### 1. A Estratégia "Híbrida" (O Diferencial Competitivo)
Decidimos não depender apenas do dataset padrão (IBM Telco). O ChurnInsight atuará em duas camadas:
* **Motor Preditivo (Compliance):** Modelo treinado no dataset oficial da IBM para prever o *Churn Score* (Quem sai?).
* **Motor Consultivo (Inovação):** Mineração proprietária de dados (Scraping) de reviews reais do mercado brasileiro para explicar a *Causa Raiz* (Por que sai?) e sugerir ações de retenção.

#### 2. Arquitetura "Mock-First"
* **Decisão:** O Backend Java não aguardará o modelo de IA estar pronto.
* **Implementação:** Criaremos interfaces de serviço que retornam dados "Mocados" (Fictícios). Isso permite que o Frontend seja construído imediatamente. Quando a IA estiver pronta, apenas trocaremos a implementação da interface (via Spring Profiles).

#### 3. Profissionalização do Workflow
* Migração do projeto pessoal para uma **GitHub Organization**.
* Adoção do **GitHub Projects (Kanban)** para gestão de tasks, saindo do informal para o rastreável.

### 🛠️ Distribuição Tática (Sprint Backlog)

| Frente | Responsável | Missão Crítica da Semana |
| :--- | :--- | :--- |
| **Data Science** | **Vlademir** | Entregar o **Baseline Model** (Regressão Logística) usando dataset IBM Telco. *Status: MVP Entregue (Acurácia Validada).* |
| **Backend** | **Raiuri / Lucas** | Estruturar DTOs, Endpoints e Contratos de API. Subir o esqueleto Spring Boot na Organization. |
| **Mock Service** | **Felipe** | Implementar o serviço de previsão simulada para desbloquear o Frontend. |
| **Intelligence** | **Philipe** | Mineração de dados não-estruturados (NLP) e orquestração da arquitetura híbrida. |

---

## 🗓️ SPRINT 00: Fundação, Arquitetura e Cultura (Demo Report)
**Data:** 11 de Dezembro de 2025 | **Fase:** Setup & Team Building

### 🚀 Resumo Executivo
A Squad 17 (NEXT HORIZON) encerra sua primeira semana (Semana 0) com sentimento de dever cumprido! Realizamos nossa Sprint Demo consolidando nossa base técnica e alinhando nossa cultura de trabalho para o Hackathon ONE.

### 🏆 Highlights da Semana

#### 1. 🏗️ Fundação Técnica & Governança
Sob a facilitação de Philipe Oliveira, estruturamos nossa "fábrica de software" adotando padrões de mercado desde o dia 1:
* **Documentação Viva:** Aprovamos o `ONBOARDING.md` e elevamos o `README.md` ao nível de Whitepaper Técnico.
* **Governança:** Regras de proteção de branch (`main`), Code Review obrigatório e Git Flow.
* **Multidisciplinaridade:** Philipe (Tech Lead) atuando de ponta a ponta (Dados, Front e DevOps) para cobrir lacunas e garantir velocidade.

#### 2. 🧠 Cultura de Inovação & AI-Driven
Realizamos um brainstorming estratégico focado em **Agentic AI**. Decidimos que o ChurnInsight não será apenas um dashboard passivo, mas uma plataforma que gera planos de retenção autônomos.

#### 3. 👥 Reconhecimento do Time
* **Felipe & Lucas (Backend):** Pela iniciativa rápida no Spring Boot e disponibilidade para pair programming.
* **Raiuri (Backend Lead):** Pela visão de arquitetura e liderança técnica no Java.
* **Rômulo (Fullstack):** Pela visão híbrida apoiando a integração.
* **Vlademir (Data Science):** Pela paixão na análise exploratória (EDA).

---

> *"Nossa meta não é apenas entregar software, é construir uma equipe de alta performance guiada por excelência e propósito."*
>
> **Assinado:** Philipe Oliveira - Tech Lead | Squad 17