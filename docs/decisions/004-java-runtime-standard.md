# ADR-004: Padronização de Runtime Java (LTS)

* **Status:** Aceito
* **Data:** 2025-12-17 (Atualizado em 2025-12-19)
* **Decisores:** Philipe Oliveira, Felipe Oliveira

## Contexto
Durante o setup do ambiente de desenvolvimento, a equipe optou por utilizar a versão mais recente e performática disponível, alinhada com a infraestrutura moderna de nuvem.

## Decisão
Padronizamos o uso do **Java 25** para todo o desenvolvimento do Backend.

## Consequências
* **Positivo:** Acesso às últimas melhorias de performance (JIT Compiler) e features sintáticas modernas.
* **Positivo:** Estabilidade garantida (sendo Java 25 a versão LTS de Setembro/2025).
* **Neutro:** Requer que todos os membros atualizem suas IDEs (IntelliJ) para suportar o SDK 25.
