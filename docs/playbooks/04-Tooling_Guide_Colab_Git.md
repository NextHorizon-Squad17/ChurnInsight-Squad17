# 📚 Guia de Versionamento: Google Colab → GitHub (Squad 17)

Este guia orienta o time de Data Science a subir notebooks (`.ipynb`) para o repositório oficial mantendo as boas práticas e a segurança da branch `main`.

**Repositório Alvo:** `NextHorizon-Squad17/ChurnInsight-Squad17`

---

## 🔒 Regra de Ouro (Segurança)

A branch `main` está **bloqueada** para escritas diretas.

- **O que acontece se tentar salvar na main:** O GitHub vai retornar `Error: Protected Branch` ou `Access Denied`.
- **A Solução:** Você deve salvar sempre em uma **Nova Branch** e depois abrir um Pull Request.

---

## 💾 Método: Salvando direto do Google Colab (Recomendado)

Você não precisa baixar o arquivo para o seu computador. O Colab faz a integração direta.

### Passo 1: Conectar ao GitHub

1. No seu Notebook aberto no Colab.
2. Vá no menu: **Arquivo (File) > Salvar uma cópia no GitHub (Save a copy in GitHub)**.
3. Se pedir autorização, autorize o acesso à sua conta.

### Passo 2: Configurar o Salvamento (Atenção Aqui!)

Uma janela vai abrir. Preencha assim:

- **Repositório:** Selecione `NextHorizon-Squad17/ChurnInsight-Squad17`.
- **Branch:** ⚠️ **NÃO DEIXE COMO `main`**.
  - Digite um nome novo para criar uma branch automaticamente.
  - *Exemplo:* `feature/random-forest-v1` ou `analysis/eda-inicial`.
- **Caminho do arquivo:** Pode deixar na raiz ou colocar numa pasta (ex: `notebooks/analise_v1.ipynb`).
- **Mensagem de Commit:** Descreva brevemente (ex: "Adiciona modelo random forest inicial").
- **Botão:** Clique em **OK**.

> **O Pulo do Gato:** Ao fazer isso, o Colab cria a branch automaticamente e salva seu código lá.

---

## 🔄 Passo 3: Abrir o Pull Request (PR)

Assim que o Colab salvar, ele vai abrir uma aba no navegador mostrando seu arquivo no GitHub.

1. Você verá um aviso amarelo: *"feature/... had recent pushes..."*.
2. Clique no botão verde **Compare & pull request**.
3. Verifique se está enviando da sua branch (`feature/...`) para a `main`.
4. Coloque um título e clique em **Create Pull Request**.

Pronto! O Tech Lead será notificado para fazer o Code Review.

---

## 💡 Dicas de Limpeza (Clean Code)

Antes de salvar, tente fazer o seguinte para deixar o repositório leve:

1. **Limpar Saídas (Opcional):** Se o gráfico for muito pesado ou tiver dados sensíveis, vá em *Editar > Limpar todas as saídas*.
2. **Nome do Arquivo:** Evite nomes como `Cópia de Untitled.ipynb`. Use nomes descritivos: `analise_exploratoria_v1.ipynb`, `modelo_random_forest.ipynb`, etc.

---

## 📋 Resumo do Fluxo

```
Colab → Nova Branch → Commit → Pull Request → Code Review → Merge na Main
```

**Dúvidas?** Entre em contato com o Tech Lead do Squad 17.