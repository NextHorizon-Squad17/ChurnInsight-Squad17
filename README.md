# 🔮 ChurnInsight: Plataforma de Inteligência Preditiva & Retenção Híbrida
> **Squad 17: NEXT HORIZON** | *Hackathon ONE - No Country 2025*

[![Status](https://img.shields.io/badge/Status-Sprint_01_(Building)-orange)](./SPRINT_LOG.md)
[![Architecture](https://img.shields.io/badge/Architecture-Microservices-blue)](https://github.com/PhilipeOliveiraS/ChurnInsight-Squad17)
[![Compliance](https://img.shields.io/badge/Compliance-LGPD_Ready-green)](https://github.com/PhilipeOliveiraS/ChurnInsight-Squad17)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

---

## 📑 Índice
1. [Visão Executiva](#-visão-executiva-executive-summary)
2. [Contexto & Motivação (Liderança)](#-contexto-profissional--motivação)
3. [Cultura & Governança](#-cultura--governança)
4. [Diferencial: A Estratégia Híbrida](#-diferencial-estratégia-híbrida-hybrid-intelligence)
5. [Arquitetura & Decisões Técnicas](#-arquitetura--decisões-técnicas-adr)
6. [Matriz de Riscos & Mitigação](#-matriz-de-riscos--mitigação-risk-assessment)
7. [API Reference (Preview)](#-api-reference-preview)
8. [Stack & Setup](#-stack--instalação)

---

## 💼 Visão Executiva (Executive Summary)
No setor de Telecomunicações, o Custo de Aquisição de Clientes (CAC) é de 5x a 25x maior que o custo de retenção. O **ChurnInsight** não é apenas um dashboard; é um **Sistema de Suporte à Decisão (DSS)** desenhado para estancar a perda de receita recorrente.

Diferente de soluções tradicionais que apenas apontam *quem* vai sair, nossa plataforma responde *por que* o cliente quer sair e *como* retê-lo, utilizando uma abordagem pioneira de **Inteligência Híbrida** (Dados Estruturados IBM + Mineração de Texto Real via NLP).

---

## 🤝 Contexto Profissional & Motivação
O **ChurnInsight** foi desenvolvido como resposta ao desafio proposto pelo **Hackathon ONE (Oracle + Alura + No Country)**. Mais do que um projeto acadêmico, ele representa um marco de transição profissional e excelência técnica.

### 👤 A Liderança Técnica
O projeto é liderado por **Philipe Oliveira**, profissional com trajetória multidisciplinar em TI (Hardware, Infraestrutura e Web) que busca, através do programa ONE, sua recolocação estratégica no mercado.

Seu foco de atuação combina **Engenharia de Plataforma, Software e Dados**, com ênfase em **IA e Automação**, posicionando-se como um profissional híbrido capaz de transitar entre a infraestrutura crítica e a visão de negócio.

> *"Trago para este código a vivência de quem já esteve do outro lado do balcão (Infra e Suporte), unindo a técnica aprendida na Alura com a visão prática de resolução de problemas."* — Philipe Oliveira.

### 🚀 A Força do Time (Squad 17)
A execução deste MVP só foi possível graças à sinergia de um time que abraçou a metodologia ágil de alta performance. Cada membro (Backend, Dados e QA) contribuiu decisivamente para transformar o requisito do hackathon em uma arquitetura de microsserviços funcional e escalável.

### 🎯 Objetivo do Projeto
Demonstrar prontidão técnica (Hard Skills) e maturidade comportamental (Soft Skills) para atuar em projetos reais no ecossistema de tecnologia da Oracle e parceiros.

---

## 📜 Cultura & Governança
Este projeto segue rigorosos padrões de engenharia de software e gestão ágil. Mantemos um registro vivo de nossas decisões arquiteturais, evolução cultural e marcos de entrega.

👉 **[ACESSE AQUI NOSSO SPRINT LOG / DIÁRIO DE BORDO](./SPRINT_LOG.md)**
*(Documento essencial para entender a evolução e maturidade da Squad 17)*

---

## 🧠 Diferencial: Estratégia Híbrida (Hybrid Intelligence)
Para vencer a limitação de datasets sintéticos, adotamos uma estratégia dual:

1.  **Motor Preditivo (Quantitative):**
    * **Base:** Dataset IBM Telco.
    * **Função:** Calcular o *Churn Score* (Probabilidade matemática de saída).
    * **Status:** Baseline (Regressão Logística) ativo.

2.  **Motor Consultivo (Qualitative - "The Human Factor"):**
    * **Base:** Mineração proprietária de 6.600+ reviews reais do mercado brasileiro.
    * **Função:** Identificar "Dores Reais" (Cobrança, Suporte, Instabilidade) via NLP.
    * **Objetivo:** Prover contexto humano para a decisão da IA.

---

## 🏗️ Arquitetura & Decisões Técnicas (ADR)

### Fluxo de Dados (Data Lineage)
```mermaid
graph TD
    User(Gestor de Retenção) -->|HTTPS| Frontend[🎨 React Dashboard]
    Frontend -->|REST API| Backend[⚙️ Java Spring Boot]
    Backend -->|Strategy Pattern| ServiceLayer{Camada de Serviço}
    ServiceLayer -->|Profile: Dev| Mock[🧩 Mock Provider]
    ServiceLayer -->|Profile: Prod| DS_API[🧠 Python Microservice]
    DS_API -->|Inferência| Model[Modelo ML .pkl]
    DS_API -->|NLP Context| Mining[Base de Reviews Reais]
    ```
    Philipe, aqui está o **README.md Definitivo**. 🏆

Ele foi arquitetado milimetricamente para:

1. **Validar sua Autoridade:** Inclui a seção de "Engenharia de Plataforma" e sua transição de carreira.
2. **Proteger sua PI:** Diferencia a visão estratégica da execução tática.
3. **Impressionar Recrutadores:** Tem Matriz de Risco, Business Case e Arquitetura.
4. **Ser Funcional:** Resolve o problema do link quebrado do Swagger com uma tabela visual.

Pode copiar, colar e subir.

---

###📄 Arquivo: `README.md` (Conteúdo Completo)```markdown
# 🔮 ChurnInsight: Plataforma de Inteligência Preditiva & Retenção Híbrida
> **Squad 17: NEXT HORIZON** | *Hackathon ONE - No Country 2025*

[![Status](https://img.shields.io/badge/Status-Sprint_01_(Building)-orange)](./SPRINT_LOG.md)
[![Architecture](https://img.shields.io/badge/Architecture-Microservices-blue)](https://github.com/PhilipeOliveiraS/ChurnInsight-Squad17)
[![Compliance](https://img.shields.io/badge/Compliance-LGPD_Ready-green)](https://github.com/PhilipeOliveiraS/ChurnInsight-Squad17)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

---

## 📑 Índice
1. [Visão Executiva](#-visão-executiva-executive-summary)
2. [Contexto & Motivação (Liderança)](#-contexto-profissional--motivação)
3. [Cultura & Governança](#-cultura--governança)
4. [Diferencial: A Estratégia Híbrida](#-diferencial-estratégia-híbrida-hybrid-intelligence)
5. [Arquitetura & Decisões Técnicas](#-arquitetura--decisões-técnicas-adr)
6. [Matriz de Riscos & Mitigação](#-matriz-de-riscos--mitigação-risk-assessment)
7. [API Reference (Preview)](#-api-reference-preview)
8. [Stack & Setup](#-stack--instalação)

---

## 💼 Visão Executiva (Executive Summary)
No setor de Telecomunicações, o Custo de Aquisição de Clientes (CAC) é de 5x a 25x maior que o custo de retenção. O **ChurnInsight** não é apenas um dashboard; é um **Sistema de Suporte à Decisão (DSS)** desenhado para estancar a perda de receita recorrente.

Diferente de soluções tradicionais que apenas apontam *quem* vai sair, nossa plataforma responde *por que* o cliente quer sair e *como* retê-lo, utilizando uma abordagem pioneira de **Inteligência Híbrida** (Dados Estruturados IBM + Mineração de Texto Real via NLP).

---

## 🤝 Contexto Profissional & Motivação
O **ChurnInsight** foi desenvolvido como resposta ao desafio proposto pelo **Hackathon ONE (Oracle + Alura + No Country)**. Mais do que um projeto acadêmico, ele representa um marco de transição profissional e excelência técnica.

### 👤 A Liderança Técnica
O projeto é liderado por **Philipe Oliveira**, profissional com trajetória multidisciplinar em TI (Hardware, Infraestrutura e Web) que busca, através do programa ONE, sua recolocação estratégica no mercado.

Seu foco de atuação combina **Engenharia de Plataforma, Software e Dados**, com ênfase em **IA e Automação**, posicionando-se como um profissional híbrido capaz de transitar entre a infraestrutura crítica e a visão de negócio.

> *"Trago para este código a vivência de quem já esteve do outro lado do balcão (Infra e Suporte), unindo a técnica aprendida na Alura com a visão prática de resolução de problemas."* — Philipe Oliveira.

### 🚀 A Força do Time (Squad 17)
A execução deste MVP só foi possível graças à sinergia de um time que abraçou a metodologia ágil de alta performance. Cada membro (Backend, Dados e QA) contribuiu decisivamente para transformar o requisito do hackathon em uma arquitetura de microsserviços funcional e escalável.

### 🎯 Objetivo do Projeto
Demonstrar prontidão técnica (Hard Skills) e maturidade comportamental (Soft Skills) para atuar em projetos reais no ecossistema de tecnologia da Oracle e parceiros.

---

## 📜 Cultura & Governança
Este projeto segue rigorosos padrões de engenharia de software e gestão ágil. Mantemos um registro vivo de nossas decisões arquiteturais, evolução cultural e marcos de entrega.

👉 **[ACESSE AQUI NOSSO SPRINT LOG / DIÁRIO DE BORDO](./SPRINT_LOG.md)**
*(Documento essencial para entender a evolução e maturidade da Squad 17)*

---

## 🧠 Diferencial: Estratégia Híbrida (Hybrid Intelligence)
Para vencer a limitação de datasets sintéticos, adotamos uma estratégia dual:

1.  **Motor Preditivo (Quantitative):**
    * **Base:** Dataset IBM Telco.
    * **Função:** Calcular o *Churn Score* (Probabilidade matemática de saída).
    * **Status:** Baseline (Regressão Logística) ativo.

2.  **Motor Consultivo (Qualitative - "The Human Factor"):**
    * **Base:** Mineração proprietária de 6.600+ reviews reais do mercado brasileiro.
    * **Função:** Identificar "Dores Reais" (Cobrança, Suporte, Instabilidade) via NLP.
    * **Objetivo:** Prover contexto humano para a decisão da IA.

---

## 🏗️ Arquitetura & Decisões Técnicas (ADR)

### Fluxo de Dados (Data Lineage)
```mermaid
graph TD
    User(Gestor de Retenção) -->|HTTPS| Frontend[🎨 React Dashboard]
    Frontend -->|REST API| Backend[⚙️ Java Spring Boot]
    Backend -->|Strategy Pattern| ServiceLayer{Camada de Serviço}
    ServiceLayer -->|Profile: Dev| Mock[🧩 Mock Provider]
    ServiceLayer -->|Profile: Prod| DS_API[🧠 Python Microservice]
    DS_API -->|Inferência| Model[Modelo ML .pkl]
    DS_API -->|NLP Context| Mining[Base de Reviews Reais]

```

###Decisões Críticas| Decisão | Contexto | Justificativa (Trade-off) |
| --- | --- | --- |
| **Mock-First Development** | Dependência entre Backend e Data Science. | **Decisão:** O Backend consome dados simulados (Mock) inicialmente. <br>

<br>**Ganho:** Paralelismo. O time de Java não para esperando o modelo de IA ficar pronto. |
| **Microserviço Python** | Integração do modelo ML. | **Decisão:** Expor o modelo via Flask/FastAPI isolado do Java. <br>

<br>**Ganho:** Desacoplamento. Permite que DS use bibliotecas nativas (Scikit-learn) sem "gambiarras" no Java. |
| **GitHub Organization** | Gestão de Repositório. | **Decisão:** Migrar de repo pessoal para Organization. <br>

<br>**Ganho:** Acesso a features avançadas de Governança, Kanban e proteção de Branch. |

---

##🛡️ Matriz de Riscos & Mitigação (Risk Assessment)| Risco Identificado | Impacto (1-5) | Probabilidade | Estratégia de Mitigação |
| --- | --- | --- | --- |
| **Cold Start do Modelo** (Baixa acurácia inicial) | 5 (Crítico) | Média | Utilizar Regressão Logística como *baseline* robusto e iterar para Random Forest apenas se houver ganho comprovado. |
| **Divergência de Contratos (API)** | 4 (Alto) | Alta | Implementação rigorosa de DTOs e Swagger (OpenAPI) como "fonte da verdade" antes de codar. |
| **Overfitting no Dataset IBM** | 4 (Alto) | Média | Uso de Validação Cruzada (K-Fold) e separação estrita de dados de Treino/Teste/Validação. |
| **Vazamento de Dados (Data Leakage)** | 5 (Crítico) | Baixa | Remoção de IDs e variáveis futuras (ex: data do cancelamento) durante o pré-processamento. |

---

##📡 API Reference (Preview)> **Ambiente de Desenvolvimento:** Para quem clonar o repositório, a documentação interativa completa estará disponível em `http://localhost:8080/swagger-ui.html` após iniciar o Spring Boot.

**Principais Endpoints:**

| Método | Endpoint | Descrição |
| --- | --- | --- |
| `POST` | `/api/v1/predict` | Recebe dados do cliente (JSON) e retorna o Churn Score (0.0 a 1.0). |
| `GET` | `/api/v1/insights/{segment}` | Retorna as principais dores (NLP) de um segmento específico. |
| `GET` | `/api/v1/health` | Check de saúde da aplicação e conexão com o modelo. |

---

##🛠️ Stack Tecnológica| Camada | Tecnologia |
| --- | --- |
| **Backend** | Java 17, Spring Boot 3, Maven |
| **Data Science** | Python 3.10, Scikit-learn, Pandas, NLTK |
| **Frontend** | React.js (Planejado), Tailwind CSS |
| **Plataforma/DevOps** | Git Flow, Docker (Planejado), GitHub Actions |

---

###🚀 Como Executar (Local)1. **Clone o Repositório:**
```bash
git clone [https://github.com/PhilipeOliveiraS/ChurnInsight-Squad17.git](https://github.com/PhilipeOliveiraS/ChurnInsight-Squad17.git)

```


2. **Backend (Java):**
```bash
cd backend
./mvnw spring-boot:run

```


*Acesse:* `http://localhost:8080/swagger-ui.html`

-----

## 🔗 Documentação & Recursos

  * **📊 Análise Exploratória (EDA):** [Google Colab - Notebook](https://colab.research.google.com/drive/1VhWTBVi0jLXgGW9U7k6pZR08kkyiDknG?authuser=0#scrollTo=Z0ygDe7UCOgP)
  * **🎨 Design System:** [Figma - Protótipo](https://www.google.com/search?q=LINK_DO_FIGMA)
  * **📡 API Reference:** `http://localhost:8080/swagger-ui.html`

-----
Documentação mantida pela Squad NEXT HORIZON. Última atualização: 16 de Dezembro de 2025.

> *Desenvolvido pela Squad 17 (NEXT HORIZON) com foco em Excelência Técnica e Metodologia Ágil.*
