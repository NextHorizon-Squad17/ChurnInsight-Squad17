#  Daily Scrum Report - 19/12/2025
**Duração:** 2h 30min (Consolidado)
**Facilitador:** Philipe Oliveira (Tech Lead)

###  Check-in de Equipe & Papéis (Atualização Tática)
* **Philipe:** Tech Lead / IA Architect / Governança.
* **Raiuri:** Backend Lead -> Migrando foco para **Cloud Infrastructure & DevOps (OCI/Docker)**.
* **Felipe & Lucas:** Backend Developers (Foco em Features & Lógica de Negócio).
* **Vlademir:** Data Science (Foco em Modelagem Avançada - XGBoost).
* **Stephanie:** Data Analyst (Foco em EDA e Tratamento de Dados).
* **Romulo:** Frontend Lead (Ausente na daily).

###  Status Report & Entregas

#### 1.  Backend (Raiuri/Felipe/Lucas)
* **Entrega Crítica:** Estrutura base da API finalizada com endpoint mocado funcional.
* **Refinamento Técnico:** Felipe corrigiu proativamente o contrato do endpoint (ajuste de Booleano para String).
* **Mentoria:** Raiuri finalizou as tasks iniciais para criar um "Gold Standard" de código para o time. Lucas está atuando em *Pair Programming* com Felipe para superar dificuldades individuais.
* **Decisão Arquitetural (Java 25):** Confirmada a decisão de manter **Java 25** (em vez de 17 LTS) visando performance, assumindo que não há restrições de infraestrutura que impeçam isso. A documentação será atualizada.

#### 2. 🧠 Data Science (Vlademir/Stephanie)
* **Caminho Crítico:** A equipe de Dados tornou-se o bloqueio principal para a integração final (dependência do arquivo \.pkl\).
* **Vlademir:** Concluiu o Random Forest. Atualmente configurando **XGBoost** e o pipeline de exportação do modelo.
* **Stephanie:** Avançando na fase de exploração (EDA) no Google Colab, seguindo o Playbook técnico.

#### 3. 🎨 Frontend (Romulo)
* **Status:** Incerto devido à ausência do lider na Daily.
* **Análise Técnica:** Code review inicial do Philipe identificou uso de *Vanilla JS + Tailwind* (divergindo do React planejado).
* **Ação de Contingência:** Tech Lead fará o build local para tentar gerar os vídeos da Sprint Demo. Caso falhe, será usada apresentação gráfica.

#### 4.  Governança & Processos
* **Horário Oficial:** Daily fixada às **18:30** para garantir quórum.
* **Comunicação:** Centralização total na plataforma oficial do Hackathon (Compliance e Rastreabilidade). Nada de decisões oficiais via WhatsApp/Discord.
* **Festividades:** Mantidas as obrigações de Sprint Demo (quintas-feiras) mesmo nas semanas de Natal/Ano Novo, com foco em reuniões concisas.

###  Impedimentos & Riscos
1.  **Emergência Pessoal (Raiuri):** Impactou a geração de documentação da sprint passada. (Mitigado: Raiuri usará o fim de semana para catch-up).
2.  **Ausência Frontend:** Falta de updates diretos do Romulo gera risco de integração.
3.  **Curva de Aprendizado (Lucas):** Dificuldade em tarefas individuais. (Mitigado via Mentoria/Pairing com Felipe).

###  Plano de Ação - Próximos Passos

####  Tech Lead (Philipe)
- [ ] Atualizar \ADR-004\ (Java Version) e \SPRINT_LOG.md\.
- [ ] Baixar e testar o código Frontend para gerar o vídeo da Sprint Demo anterior.
- [ ] Gerar relatório oficial da Sprint Demo pendente.

####  Infra & Backend (Raiuri/Felipe/Lucas)
- [ ] **Raiuri:** Desenhar arquitetura Cloud (OCI) e apresentar no Planning de segunda.
- [ ] **Felipe/Lucas:** Detalhar tarefas de Autenticação e Banco de Dados para a próxima Sprint.

####  Data Science (Vlademir/Stephanie)
- [ ] **Vlademir:** Finalizar e exportar o modelo \.pkl\ (Prioridade Máxima).
- [ ] **Stephanie:** Gerar primeiras visualizações ricas do dataset até segunda-feira.

---
