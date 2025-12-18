# ADR-004: Padronização de Runtime Java (LTS)

* **Status:** Aceito
* **Data:** 2025-12-17
* **Decisores:** Philipe Oliveira, Felipe Oliveira

## Contexto
Durante o setup do ambiente de desenvolvimento, membros da equipe enfrentaram incompatibilidades e erros de execução ao utilizar o JDK 24 (versão "bleeding edge").
Isso gerou tempo ocioso tentando configurar o ambiente em vez de codar.

## Decisão
Padronizamos o uso do **Java 17 LTS (Long Term Support)** para todo o desenvolvimento do Backend.

## Consequências
* **Positivo:** Estabilidade garantida e compatibilidade com a maioria das bibliotecas Spring Boot.
* **Positivo:** Facilita o deploy em containers e nuvem, que geralmente suportam melhor versões LTS.
* **Negativo:** Perda de features sintáticas muito novas do Java 21/24 (aceitável dado o escopo do projeto).
