# ADR-002: Estratégia de Desenvolvimento Frontend Mock-First

* **Status:** Aceito
* **Data:** 2025-12-17
* **Decisores:** Philipe Oliveira, Rômulo Felipe

## Contexto
A equipe de Backend está em fase inicial de estruturação da API e DTOs.
A Sprint Demo exige a apresentação de uma interface funcional e navegável para validar a UX/UI com os stakeholders.
Havia o risco de chegar na Demo sem nada visual para mostrar devido à dependência do Backend.

## Decisão
Adotamos a estratégia **Mock-First Development** para o Frontend.
O Frontend deve ser construído consumindo arquivos JSON estáticos ou objetos mockados hardcoded, baseados no contrato de dados (DTO) acordado, em vez de esperar a API real estar online.

## Consequências
* **Positivo:** Desbloqueia o trabalho do Frontend imediatamente (Paralelismo).
* **Positivo:** Garante entrega visual para a Sprint Demo independente de falhas no Backend.
* **Negativo:** Gera débito técnico de integração (será necessário refatorar para conectar na API real depois).
