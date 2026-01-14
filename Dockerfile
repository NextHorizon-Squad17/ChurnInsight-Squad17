# Dockerfile atualizado para sua estrutura de pastas
FROM python:3.10-slim

WORKDIR /app

# Instala dependências do sistema
RUN apt-get update && apt-get install -y libgomp1

# 1. Copia e instala requisitos (da raiz data-science)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copia a API (da pasta api para a raiz do container)
COPY data-science/api/main.py .

# 3. Copia o Modelo (da pasta model para a raiz do container)
COPY data-science/model/churn_model_final.pkl .

# 4. Copia o .env (da raiz data-science)
COPY .env .

# Expõe a porta
EXPOSE 8000

# Roda a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]