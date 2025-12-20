

# 📜 SPRINT LOG & ARCHITECTURAL JOURNEY | SQUAD 17

> **Documento Vivo:** Este log registra a evolução estratégica, técnica e cultural do projeto **ChurnInsight**. Aqui documentamos não apenas o código, mas as decisões de arquitetura e governança tomadas pela liderança e pelo time.

---


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