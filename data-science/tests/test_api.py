import os
import sys
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

# 1. Configuração de Caminho
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.main import app

# 2. Inicializa o Cliente de Teste (CORREÇÃO DE SINTAXE)
# Em versões novas do Starlette/FastAPI, passamos o app como argumento posicional ou usamos 'transport'
# A forma mais compatível e simples é passar direto:
client = TestClient(app)

# Se der erro de 'transport' no futuro, a alternativa seria:
# client = TestClient(transport=ASGITransport(app=app), base_url="http://test")

# --- TESTES DE SAÚDE ---
def test_health_check():
    """Verifica se a API está de pé."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

# --- TESTES DE PREDIÇÃO ---
@patch("api.main.generate_retention_plan")
def test_predict_churn_high_risk(mock_genai):
    """Teste de um cliente com perfil de ALTO RISCO."""
    
    mock_genai.return_value = "PLANO SIMULADO: Oferecer desconto."

    payload = {
        "Gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "No",
        "Dependents": "No",
        "TenureMonths": 1,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "Yes",
        "StreamingMovies": "Yes",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 100.00,
        "TotalCharges": 100.00
    }

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    data = response.json()
    
    assert "prediction" in data
    assert "probability" in data
    assert data["retention_strategy"] == "PLANO SIMULADO: Oferecer desconto."

# --- TESTES DE VALIDAÇÃO ---
def test_predict_validation_error():
    """Verifica se a API rejeita dados inválidos."""
    payload = {
        "Gender": "Alien", # Inválido
        "SeniorCitizen": 0,
        "Partner": "Yes",
        "Dependents": "No",
        "TenureMonths": 12,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 70.0,
        "TotalCharges": 800.0
    }

    response = client.post("/predict", json=payload)
    
    # 422 = Unprocessable Entity (Erro de validação do Pydantic)
    assert response.status_code == 422