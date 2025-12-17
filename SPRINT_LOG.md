

# 📜 SPRINT LOG & ARCHITECTURAL JOURNEY | SQUAD 17

> **Documento Vivo:** Este log registra a evolução estratégica, técnica e cultural do projeto **ChurnInsight**. Aqui documentamos não apenas o código, mas as decisões de arquitetura e governança tomadas pela liderança e pelo time.

---

## 📅 Daily Scrum Report - 16/12/2025
**Duração:** ~2h 45min
**Facilitador:** Philipe Oliveira (Tech Lead)

### 👥 Check-in de Equipe & Papéis (Definidos na Daily)
* **Philipe:** Tech Lead / Platform Engineering / Data Science.
* **Raiuri:** Lead de Backend (Delegado pelo Tech Lead).
* **Romulo:** Lead de Frontend / UX (Apresentou protótipo visual).
* **Vlademir:** Data Science (Foco em Modelagem ML).
* **Stephanie:** Data Science / Dados (Onboarding iniciado).
* **Lucas:** Backend Developer (Foco em DTOs/Contratos).
* **Felipe:** Backend Developer (Foco em Mock/Lógica).

### 🚀 Status Report & Entregas
1.  **Backend (Raiuri/Lucas/Felipe):**
    * **Impedimento Crítico:** O monorepo atual gerou conflitos de IDE e `.gitignore` para o time de Java.
    * **Decisão Arquitetural:** Raiuri propôs e o time acatou a separação do Backend Java em um repositório dedicado dentro da Organização para destravar o desenvolvimento.
    * **Progresso:** Lucas já estruturou localmente os `Controllers` e `DTOs`. Felipe já possui a lógica dos dados mockados, aguardando apenas o endpoint.

2.  **Data Science (Vlademir/Stephanie/Philipe):**
    * **Vlademir:** Concluiu o baseline (Regressão Logística). Iniciará a implementação do *Random Forest* para comparar a acurácia.
    * **Stephanie:** Iniciou o onboarding. Tarefa imediata é consumir a documentação (Sprint Log/Readme) e o Notebook do Colab para se integrar.

3.  **Frontend/UX (Romulo):**
    * **Demo Apresentada:** Romulo compartilhou tela mostrando uma interface funcional com simulação de entrada de dados, cálculo de risco de churn e *Dark/Light Mode* implementado.
    * **Ação:** Instruído pelo Tech Lead a subir o código imediatamente, mesmo que incompleto, para registrar atividade.

### 🎯 Plano de Ação - Próximas 24 Horas (Tarefas Distribuídas)

#### 👨‍💻 Tech Lead (Philipe)
- [ ] **Infra:** Criar a GitHub Organization `NextHorizon-Squad17`.
- [ ] **Multi-Repo:** Criar os repositórios `ChurnInsight-Backend` e `ChurnInsight-Frontend` na Org.
- [ ] **Access:** Adicionar todos os membros (via e-mail) na Organização e configurar permissões.
- [ ] **Docs:** Atualizar README principal linkando os novos repositórios.

#### ☕ Squad Backend (Liderança: Raiuri)
- **Raiuri:**
    - [ ] Subir a estrutura base ("esqueleto") do Spring Boot no novo repositório de Backend.
    - [ ] Configurar o *Project Board* com as tarefas de backend distribuídas para Felipe e Lucas.
    - [ ] Enviar e-mail para convite da Org.
- **Lucas:**
    - [ ] Migrar o código local (DTOs/Controllers) para o novo repositório assim que o Raiuri subir a base.
    - [ ] Finalizar a definição dos contratos (`CustomerDTO`, `ChurnResponseDTO`) até o fim da semana.
- **Felipe:**
    - [ ] Integrar a lógica de *Mock Data* (JSON) no endpoint que o Lucas vai criar.
    - [ ] Realizar Pull Request da feature de Mock no novo repositório.

#### 🎨 Squad Frontend (Liderança: Romulo)
- **Romulo:**
    - [ ] Enviar e-mail pendente para convite da Org.
    - [ ] Inicializar o repositório `ChurnInsight-Frontend` com a estrutura React/Vite.
    - [ ] Realizar **Push** do código apresentado na Daily (Tela de Simulação + Dark Mode) para garantir contribuição no gráfico do GitHub.

#### 🧠 Squad Data Science (Liderança: Philipe/Vlademir)
- **Vlademir:**
    - [ ] Treinar modelo *Random Forest* no Colab.
    - [ ] Gerar relatório comparativo de acurácia (Baseline vs Random Forest).
- **Stephanie:**
    - [ ] Enviar e-mail pendente para convite da Org.
    - [ ] Leitura completa do `SPRINT_LOG.md` e histórico do chat para nivelamento.
    - [ ] Acessar o Google Colab do projeto e rodar as células para validar o ambiente.
    - [ ] Definir com Philipe qual tarefa específica de dados irá assumir após o estudo inicial.

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