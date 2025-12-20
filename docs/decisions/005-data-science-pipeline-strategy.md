# ADR-005: Estratégia de Pipeline de Data Science em Camadas

* **Status:** Aceito
* **Data:** 2025-12-18
* **Decisores:** Philipe Oliveira (Tech Lead)

## Contexto
O desafio de Churn exige alta precisão e explicabilidade. Equipes tradicionais de Hackathon tendem a trabalhar em silos ou todos no mesmo notebook, gerando conflitos e código não produtivo.

## Decisão
Adotamos uma arquitetura de **Pipeline em Camadas Especializadas**, segregando responsabilidades:
1.  **Camada de Fundação (Data Analyst):** Foco exclusivo em EDA, Limpeza e Feature Engineering.
2.  **Camada de Benchmark (ML Engineer):** Foco em modelos clássicos (Ensemble) e balanceamento de classes.
3.  **Camada de Inovação (AI Architect):** Foco em Deep Learning, XAI (Explicabilidade) e MLOps (API).

## Consequências
* **Positivo:** Paralelismo total (membros não se bloqueiam).
* **Positivo:** Gestão de Risco (se Deep Learning falhar, temos o Benchmark robusto).
* **Positivo:** Onboarding acelerado de membros juniores através de Playbooks dedicados.
