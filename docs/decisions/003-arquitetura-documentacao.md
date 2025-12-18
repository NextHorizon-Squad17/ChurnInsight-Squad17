# ADR-003: Arquitetura de Documentação Segregada (Enterprise Standard)

* **Status:** Aceito
* **Data:** 2025-12-17
* **Decisores:** Philipe Oliveira (Tech Lead)

## Contexto
Inicialmente, toda a documentação de progresso era centralizada num único arquivo \SPRINT_LOG.md\.
Conforme o projeto escalou, este arquivo misturou registros históricos (dailies), planejamentos futuros e decisões técnicas, dificultando a leitura e a auditoria por parte dos avaliadores.

## Decisão
Reestruturamos a pasta \docs/\ seguindo o padrão corporativo de segregação temporal:
1.  **\docs/dailies/\**: Registro imutável do passado (Atas de reunião).
2.  **\docs/plans/\**: Planejamento tático do futuro (Estratégias de Demo).
3.  **\docs/decisions/\**: Registro lógico de arquitetura (ADRs).

## Consequências
* **Positivo:** Melhora a navegabilidade e a organização do repositório.
* **Positivo:** Facilita a auditoria externa (Banca Avaliadora).
* **Negativo:** Exige disciplina do time para salvar os arquivos nas pastas corretas.
