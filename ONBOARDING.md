# 🚀 SQUAD 17: NEXT HORIZON | PROJETO CHURNINSIGHT
> **Hackathon ONE - No Country 2025** | *Data Driven & AI Solutions*

![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-blue)
![Fase](https://img.shields.io/badge/Fase-MVP_Core-orange)
![Deadline Final](https://img.shields.io/badge/Entrega_Final-18_Jan_2026-red)

---

## 🎯 1. NOSSA MISSÃO: DESAFIO 2 (ChurnInsight)
**Objetivo:** Construir uma solução preditiva para retenção de clientes.
* **O Problema:** Prever cancelamentos (Churn) antes que aconteçam.
* **A Solução:** Uma API de IA que calcula a probabilidade de churn e gera estratégias de retenção.
* **Diferencial Competitivo:** Uso de **IA Generativa** para criar planos de ação personalizados para retenção.

---

## 📅 2. NOSSO CRONOGRAMA MACRO (6 SEMANAS)
[cite_start]*Baseado no Regulamento Oficial* [cite: 900, 40]

* **Semana 1 (Atual):** Setup, Arquitetura, EDA (Dados) e Esqueleto API.
* **Semana 2:** MVP Funcional (API Java + Modelo Simples + Front Básico).
* **Semana 3:** Integração Total e Deploy na Nuvem (OCI).
* **Semana 4:** Implementação do Diferencial (Relatório IA com Gemini).
* **Semana 5:** Testes, Refinamento e Feedback 360º.
* **Semana 6:** Gravação do Vídeo Demo e preparação para o Demo Day (20/01).

---

## ⚙️ 3. ARQUITETURA DE SOFTWARE (PROFISSIONAL)

### Backend (Java Spring Boot)
* **Arquitetura:** MVC (Model-View-Controller) com Camadas (Controller -> Service -> Repository).
* **Segurança:** Validação de input (DTOs com Bean Validation).
* **Banco de Dados:** MySQL (Hospedado na OCI).

### Data Science (Python)
* **Modelo:** Classificação Supervisionada (Random Forest/Logistic Regression).
* **Entrega:** Microserviço API (Flask/FastAPI) que expõe o modelo `.pkl` para o Backend.

### Frontend (React)
* **Interface:** Dashboard Administrativo para gestores visualizarem o risco de churn.

*"Nossa meta não é apenas entregar, é ser a referência técnica do Hackathon."*
---

## 🚨 4. ROTINA E OBRIGAÇÕES (PARA APROVAÇÃO)
[cite_start]*Regras do Guia da Plataforma* [cite: 48, 49, 100-105]

1.  **Daily Meeting (18:00h):** Alinhamento rápido de 15min. (Quem não puder, avise no chat).
2.  **Sprint Demo (Quinta-feira):** Apresentação obrigatória do progresso da semana.
3.  **Registro na Plataforma:** **CRUCIAL.** Entre todo dia na aba "Cronograma" e marque suas tarefas como concluídas. Sem isso, você é eliminado.
4.  **Comunicação:** Usem o chat da No Country para registrar presença.

---
## 🧬 5. DIRETRIZES DE DATA SCIENCE (ANTI-DESCLASSIFICAÇÃO)
*Regras cruciais para garantir a validade técnica do nosso modelo.*

### 🚨 A "Armadilha" do Dataset (Data Leakage)
Para evitar que nosso projeto seja invalidado por "vício de dados" ou vazamento de resposta, o time de Dados deve seguir rigorosamente:

1.  **Sanitização de Colunas:** Remover qualquer coluna que entregue a resposta ("Churn Reason", "Churn Score" pré-calculado por terceiros). O modelo deve aprender com o *comportamento* (pagamentos, uso), não com a resposta pronta.
2.  **Atenção ao CLTV:** Se usarmos *Lifetime Value*, devemos garantir que ele seja calculado com dados históricos *anteriores* ao evento de churn. Se o dataset já vier com isso pronto, precisamos validar se não é um dado "viciado".
    * *Regra de Ouro:* "Eu teria esse dado no momento da predição?" Se a resposta for não, remova a coluna.

### 📓 Ambiente de Desenvolvimento Obrigatório (Google Colab)
[cite_start]Conforme o Regulamento [cite: 785-786, 940], a entrega oficial de Data Science **NÃO** é apenas o modelo final, mas a **história da análise**.

* **Ferramenta:** Todo o desenvolvimento (EDA, Treino, Teste) deve ser feito no **Google Colab**.
* **Por que:** O Colab permite que os avaliadores rodem o código na nuvem sem configurar ambiente local.
* **Entregável:** O arquivo `.ipynb` (Notebook) deve estar bem documentado (com textos explicando o raciocínio em cada bloco de código) e o link deve constar no `README.md` oficial.

> **Meta:** Nosso notebook deve ser uma "aula" de como chegamos na previsão, provando que não usamos atalhos proibidos.
---

## 🔗 5. LINKS E RECURSOS
* [📄 Regulamento Oficial (PDF)](https://empresas.alura.com.br/hubfs/G8%20-%20BRA%20-%20Regulamento%20do%20Hackathon%20ONE%20V2%20%E2%80%93%20No%20Country%202025.pdf)
* [🗓️ Guia da Plataforma (PDF)](https://drive.google.com/file/d/1eOZYn4Fb5pgX7xmrdcmSjQjIqd6VAnnm/view?pli=1)
* [💻 Repositório GitHub](https://github.com/PhilipeOliveiraS/ChurnInsight-Squad17)
* [🎨 Design (Figma)](LINK)

*> Superar a expectativa do cliente é o que transforma código em negócio." - NEXT HORIZON Team*