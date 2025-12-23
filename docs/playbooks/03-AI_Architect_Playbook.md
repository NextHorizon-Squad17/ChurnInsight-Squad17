#  Guia de Missão: Lead AI Researcher & MLOps Architect

**Para:** Philipe Oliveira (PH)  
**Contexto:** Hackathon ONE 2025 - Projeto ChurnInsight

---

##  Sua Importância na Equipe
Você é o "Closer".

Enquanto a Stephanie prepara o terreno e o Vlademir constrói as paredes seguras (o Baseline), você é responsável pelo teto de vidro e pela eletricidade.

* **Inovação:** O seu modelo de Deep Learning é o que vai brilhar nos olhos dos jurados como "Tecnologia de Ponta".
* **Viabilidade:** É o seu código de API (MLOps) que vai permitir que o Backend Java consuma a inteligência. Sem isso, temos apenas um notebook, não um produto.
* **Segurança:** Se os modelos deles falharem, você precisa ter a capacidade técnica de corrigir ou pivotar a solução em minutos.

---

##  O Mapa da Jornada (O Caminho da Vitória)
Sua execução técnica deve ser cirúrgica. Não desperdice tempo testando coisas básicas; foque na complexidade que traz valor.

###  Missão 1: A Mente Artificial (Deep Learning Architecture)
* **O Conceito:** Superar os limites dos modelos clássicos (Random Forest) capturando não-linearidades complexas através de camadas neurais profundas.
* **Sua Tarefa:** Construir e treinar uma Rede Neural (MLP - Multilayer Perceptron) do zero.

**A Arquitetura: Não use padrões. Desenhe a rede.**
1.  **Input:** O número de features tratadas pela Stephanie.
2.  **Hidden Layers:** Projete uma estrutura de funil (ex: 128 -> 64 -> 32 neurônios). Use ativação ReLU ou Swish (mais moderna).
3.  **Output:** 1 neurônio com ativação Sigmoid (para probabilidade de 0 a 1).

**Otimização de Treino:**
* **Dropout:** Adicione camadas de Dropout (20-30%) para evitar que a rede decore os dados (*overfitting*).
* **Early Stopping:** Configure o treinamento para parar automaticamente se a validação parar de melhorar. Não gaste GPU à toa.
* **Framework:** TensorFlow/Keras ou PyTorch. (Keras é mais rápido para prototipar no Hackathon).

> 💡 **Dica de Mestre:** Se o seu modelo de Deep Learning performar pior que o Random Forest do Vlademir (o que é comum em dados tabulares), não se desespere. Use isso na narrativa: *"Testamos Deep Learning, mas provamos que Ensemble Trees performam melhor para este dataset específico, demonstrando maturidade de decisão técnica"*.

### 🔮 Missão 2: A Caixa de Vidro (Explainable AI - XAI)
* **O Conceito:** O maior medo de um CEO é uma IA que toma decisões que ninguém entende ("Black Box"). Vamos quebrar isso.
* **Sua Tarefa:** Implementar SHAP (SHapley Additive exPlanations).

**Integração:** Aplique a biblioteca shap no seu modelo (ou no do Vlademir, se for o escolhido para produção).

**O "Porquê":** Não quero apenas Churn: Sim. Quero:
> Churn: **Sim**
> * Motivo 1: Idade > 50 (+0.3 risco)
> * Motivo 2: Produtos = 1 (+0.2 risco)

**Visualização:** Gere o *Force Plot* ou *Beeswarm Plot* para colocar no Slide da apresentação. Isso ganha o jogo.

### ⚙️ Missão 3: A Ponte (MLOps & API Strategy)
* **O Conceito:** O Squad Java (Raiuri/Lucas) precisa chamar sua IA como se fosse um site. Eles não rodam Python.
* **Sua Tarefa:** Produtizar o modelo.

1.  **Serialização:** Salve o modelo treinado (model.h5 ou model.pkl) e os pre-processadores da Stephanie (o Scaler e o Encoder). **Atenção:** Se você não salvar o Scaler, não conseguirá tratar os dados novos que chegarem pela API.
2.  **FastAPI:** Crie um microserviço ultra-rápido.
    * POST /predict: Recebe JSON do cliente -> Aplica Scaler -> Roda Modelo -> Retorna JSON com probabilidade e explicação SHAP.
3.  **Docker (O Diferencial):** Crie um Dockerfile simples.
    * *Por que?* Para garantir que roda na nuvem ou na máquina do avaliador sem erros de "biblioteca faltando".

---

## 🤖 Manual de Uso da IA (O Copiloto do Arquiteto)
Como Sênior, você não pede código básico. Você pede **Crítica Arquitetural**.

**✅ O Jeito TECH LEAD de usar**
* **Revisão de Segurança:** *"Analise este código FastAPI. Existem vulnerabilidades de injeção ou problemas de concorrência nas chamadas assíncronas?"*
* **Otimização:** *"Esta função de pré-processamento Pandas está lenta (O(n^2)). Reescreva usando vetorização numpy para ser O(n)."*
* **Boilerplate de Teste:** *"Gere testes unitários (Pytest) para verificar se minha API quebra quando recebe nulos no JSON."*

---

## 📚 Fontes de Pesquisa de Alto Nível
Saia do básico. Vá onde a indústria está.

1.  **Papers with Code:** Procure por "Tabular Data Deep Learning". Veja o que há de mais novo (ex: TabNet) se quiser ousar.
2.  **Netflix Tech Blog / Uber Engineering:** Pesquise como eles colocam modelos em produção. Use os termos deles ("Inference pipeline", "Model serving") no seu Pitch.
3.  **ArXiv:** Se precisar entender a matemática profunda por trás do SHAP para explicar para a banca.

---

## ✅ Checklist do Comandante (Definition of Done)
Você só descansa quando isso estiver pronto:

- [ ] Pipeline de Treinamento Neural rodando (com Loss diminuindo).
- [ ] Implementação do SHAP funcionando (gerando explicações locais).
- [ ] API FastAPI rodando localmente (recebe JSON, devolve Previsão).
- [ ] Serialização correta (Modelo + Scalers salvos).
- [ ] **Code Review:** Revisou o PR da Stephanie (EDA) e do Vlademir (Baseline) e deu feedback construtivo.
- [ ] **Integração:** Testou a chamada da API junto com o Raiuri (Backend Java).

Philipe, a equipe confia na sua visão. A arquitetura está desenhada. Agora, é hora de liderar pelo exemplo e codar o futuro. **Execute.** 
