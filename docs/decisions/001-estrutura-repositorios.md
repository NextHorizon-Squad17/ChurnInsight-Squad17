# ADR-001: Estratégia de Repositórios e Governança de Branch

* **Status:** Aceito
* **Data:** 2025-12-17
* **Decisores:** Philipe Oliveira (Tech Lead), Raiuri (Back Lead), Rômulo (Front Lead)

## Contexto
O projeto ChurnInsight envolve múltiplas disciplinas (Data Science, Backend Java, Frontend React).
Inicialmente, precisávamos decidir entre manter um único repositório (Monorepo) ou separar as responsabilidades, além de definir como garantir a qualidade do código na branch principal.

## Decisão
Decidimos adotar a estratégia de **Multi-Repo** com **Branch Protection** ativada.

1.  **Estrutura:**
    * \ChurnInsight-Squad17\ (Data Science & Documentação Central)
    * \ChurnInsight-Backend\ (API Java Spring)
    * \ChurnInsight-Frontend\ (React Web)

2.  **Governança:**
    * Branches \main\ e \develop\ foram bloqueadas para push direto.
    * Obrigatoriedade de **Pull Request (PR)** com no mínimo 1 aprovação para merge.

## Consequências
* **Positivo:** Isola o ambiente de desenvolvimento (o Front não quebra o Back).
* **Positivo:** Força Code Review, aumentando a qualidade do código e compartilhamento de conhecimento.
* **Negativo:** Aumenta a complexidade de gestão (3 repositórios em vez de 1), mitigada pelo uso de Git Submodules ou links na documentação central.
