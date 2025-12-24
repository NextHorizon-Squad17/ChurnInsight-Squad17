#  Relatório Executivo da Daily Scrum: Projeto ChurnInsight (24/12/2025)

**Facilitador:** Philipe Oliveira (Tech Lead)
**Status do Projeto:**  AMARELO (Atenção - Prazo de Integração)
**Foco Tático:** Desbloqueio de Dependências & Integração End-to-End

---

## 1.0 Resumo Executivo
Este relatório oferece uma visão estratégica sobre o status do Projeto ChurnInsight no momento crítico de integração entre Backend e IA.

**Status: Amarelo / Atenção**
A classificação se justifica pela janela de oportunidade restrita pré-feriado. Observou-se uma mudança tática crucial: a equipe evoluiu de um modelo de "Desenvolvimento Isolado" para uma **"Força-Tarefa de Integração"**, onde a prioridade absoluta é unificar os módulos em um serviço coeso.

---

## 2.0 Squad Pulse: Status Report por Frente

###  Backend (Raiuri, Lucas)
* **Estratégia de Redundância:** Devido ao prazo crítico, Lucas e Felipe adotaram uma estratégia de **Desenvolvimento Paralelo** para o módulo de Autenticação, visando convergência posterior do melhor código.
* **Infraestrutura:** Raiuri atuou como agente de *de-risking*, padronizando o ambiente com **Docker** para eliminar falhas de configuração ("works on my machine") e apoiar a IA.
* **Entregas:** Endpoints iniciais de login e predict mapeados.

###  Data Science (Vlademir, Stephanie)
* **Marco Técnico:** Vlademir finalizou a lógica do modelo.
* **Cross-Functional Support:** Houve um bloqueio crítico de permissões entre Google Colab e GitHub. O time de Backend (Raiuri) interveio para configurar o ambiente local (VS Code), permitindo o push do código. Isso demonstra a resiliência do time.
* **Próximo Passo:** Serialização do modelo (.pkl) aguardando validação do Tech Lead.

###  Frontend (Romulo)
* **Status:** Em pausa estratégica devido à ausência programada. Depende da liberação dos endpoints reais para substituir os mocks.

### 👨‍💻 Liderança Técnica (Philipe)
* **Atuação:** Tech Lead operando como **"Enabler"**.
* **Foco Imediato:** Code Review do modelo de IA (Prioridade 0) para destravar a serialização e, consequentemente, o Backend. Compromisso de entrega antes do feriado.

---

## 3.0 Decisões Arquiteturais & Técnicas (Engineering Showcase)

### 3.1 Padrão "Contract-First"
A liderança técnica definiu o contrato de dados (JSON Schema) *antes* da codificação final.
* **Impacto:** Transformou o risco de integração em um fluxo gerenciável, permitindo que Java e Python avancem sem bloqueios mútuos totais.

### 3.2 Ecossistema de Alta Performance
* **Pickle:** Padrão de serialização nativa para performance máxima no carregamento do modelo.
* **Docker:** Garantia de consistência entre ambientes de desenvolvimento e produção (OCI).

---

## 4.0 Gestão de Riscos & Mitigação

| Risco Principal | Plano de Ação |
| :--- | :--- |
| **Atraso na Integração (Natal)** | **Força-Tarefa:** Intervenção direta de membros seniores (Raiuri/Philipe) para desbloquear tarefas de juniores. |
| **Bloqueio de Code Review** | **Priorização:** Tech Lead realocou agenda para validar o modelo de IA até sexta-feira, garantindo o *deploy* do artefato. |

---
*Este documento consolida a transparência e a maturidade de engenharia do Squad 17.*
