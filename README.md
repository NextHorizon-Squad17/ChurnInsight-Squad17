# 🔮 ChurnInsight: Plataforma de Inteligência Preditiva
> **Squad 17: NEXT HORIZON** | *Hackathon ONE - No Country 2025*

[![Status](https://img.shields.io/badge/Status-MVP_Em_Desenvolvimento-orange)](https://github.com/PhilipeOliveiraS/ChurnInsight-Squad17)
[![Stack](https://img.shields.io/badge/Stack-Java_Spring_|_Python_AI-blue)](https://github.com/PhilipeOliveiraS/ChurnInsight-Squad17)
[![Infrastructure](https://img.shields.io/badge/Infra-Oracle_Cloud_(OCI)-red)](https://github.com/PhilipeOliveiraS/ChurnInsight-Squad17)

---

## 🎯 O Desafio de Negócio
No setor de serviços recorrentes (Telecom, SaaS), a evasão de clientes (**Churn**) representa um impacto financeiro direto e muitas vezes silencioso. As empresas tradicionalmente reagem de forma tardia, atuando apenas após o cancelamento.

**O Objetivo:** Mudar o paradigma de "Reação Pós-Cancelamento" para "Retenção Preditiva", identificando padrões comportamentais de risco antes que a decisão de saída seja tomada.

---

## 💡 Nossa Solução (Value Proposition)
O **ChurnInsight** é um **Ecossistema de Decisão Baseado em Dados**. Diferente de dashboards passivos, nossa plataforma atua como um motor de inteligência que integra análise preditiva e prescritiva:

* **Visão de Negócio:** Dashboard executivo com análise de causa raiz e segmentação de risco.
* **Inteligência Preditiva:** Algoritmos de Machine Learning que calculam a probabilidade de saída em tempo real.
* **Ação Prescritiva (GenAI):** Integração com **IA Generativa (Google Gemini)** que analisa o perfil do cliente crítico e gera, automaticamente, um **Plano de Retenção Personalizado** para a equipe de atendimento.

---

## 🏗️ Arquitetura de Solução
O sistema foi desenhado seguindo princípios de **Arquitetura de Microsserviços**, garantindo desacoplamento, escalabilidade e manutenibilidade:

1.  **🧠 Cérebro (Data Science):** Modelo de Classificação Supervisionada (**Random Forest**) treinado em Python, exposto via API de alta performance (FastAPI).
2.  **⚙️ Motor (Backend):** API REST em **Java 17 (Spring Boot)** responsável pela orquestração de regras de negócio, validação de dados e segurança.
3.  **🎨 Interface (Frontend):** Aplicação SPA em **React**, focada em usabilidade e visualização de dados críticos.
4.  **☁️ Infraestrutura:** Containerização via Docker e orquestração na **Oracle Cloud Infrastructure (OCI)**.

### 🧩 Fluxo de Dados (Data Lineage)

```mermaid
graph TD
    User(Gestor) -->|HTTPS| Frontend[🎨 Dashboard React]
    Frontend -->|JSON Payload| Backend[⚙️ API Gateway Spring Boot]
    Backend -->|Persistência| DB[(Oracle Database)]
    Backend -->|Request| DS_API[🧠 Microserviço Python]
    DS_API -->|Inferência| Model[Modelo ML .pkl]
    DS_API -->|Enrichment| GenAI[Google Gemini]
    DS_API -->|Insight Acionável| Backend
    Backend -->|Resposta| Frontend
````

-----

## 🗂️ Engenharia de Dados

Utilizamos uma versão enriquecida do dataset padrão da indústria (**IBM Telco Churn**), submetido a um rigoroso processo de ETL e Feature Engineering.

  * **Volume:** 7.043 registros processados.
  * **Target:** `Churn` (Variável binária).
  * **Features Críticas:** Longevidade do contrato, método de pagamento e histórico de suporte.

-----

## 🛠️ Stack Tecnológica

| Camada | Tecnologia |
| :--- | :--- |
| **Backend** | Java 17, Spring Boot 3 (MVC), Bean Validation, Swagger/OpenAPI |
| **Data / AI** | Python 3.10, Scikit-learn (Random Forest), Pandas, Google Gemini API |
| **Frontend** | React.js, Tailwind CSS |
| **DevOps** | Docker, OCI (Oracle Cloud), Git Flow |

-----

## 🚀 Setup e Instalação

### Pré-requisitos

  * Java 17+ e Maven
  * Python 3.10+
  * Node.js 18+
  * Docker (Opcional para ambiente containerizado)

### Execução Local

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/PhilipeOliveiraS/ChurnInsight-Squad17](https://github.com/PhilipeOliveiraS/ChurnInsight-Squad17)
    ```

2.  **Backend (API):**

    ```bash
    cd backend
    mvn spring-boot:run
    ```

3.  **Frontend (Interface):**

    ```bash
    cd frontend
    npm install && npm start
    ```

4.  **Acesso:** O sistema estará disponível em `http://localhost:3000`.

-----

## 🔗 Documentação & Recursos

  * **📊 Análise Exploratória (EDA):** [Google Colab - Notebook](https://www.google.com/search?q=LINK_DO_COLAB)
  * **🎨 Design System:** [Figma - Protótipo](https://www.google.com/search?q=LINK_DO_FIGMA)
  * **📡 API Reference:** `http://localhost:8080/swagger-ui.html`

-----
Documentação mantida pela Squad NEXT HORIZON. Última atualização: 11 de Dezembro de 2025.

> *Desenvolvido pela Squad 17 (NEXT HORIZON) com foco em Excelência Técnica e Metodologia Ágil.*
