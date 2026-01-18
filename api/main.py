import os
import pickle
import pandas as pd
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.genai as genai
from google.genai.types import GenerateContentConfig
from dotenv import load_dotenv

load_dotenv()
app = FastAPI(title="ChurnInsight Intelligence API", version="2.0 - Full Features")

EXCEL_PATH = "Telco_customer_churn.xlsx"

GEMINI_KEY = os.getenv("GOOGLE_API_KEY")

if not GEMINI_KEY:
    print("⚠️ AVISO: GOOGLE_API_KEY não encontrada no .env")

MODEL_PATH = "churn_model_final.pkl"

try:
    with open(MODEL_PATH, "rb") as f:
        pipeline = pickle.load(f)
    print("✅ Modelo carregado!")
except FileNotFoundError:
    print(f"⚠️ Modelo não encontrado: {MODEL_PATH}")
    pipeline = None

class CustomerData(BaseModel):
    # Dados Pessoais
    Gender: str
    SeniorCitizen: int # 0 ou 1
    Partner: str       # "Yes" ou "No"
    Dependents: str    # "Yes" ou "No"
    
    # Dados de Serviço
    TenureMonths: int  # Era 'Tenure'
    PhoneService: str
    MultipleLines: str
    InternetService: str
    OnlineSecurity: str
    OnlineBackup: str
    DeviceProtection: str
    TechSupport: str
    StreamingTV: str
    StreamingMovies: str
    
    # Dados de Contrato e Financeiro
    Contract: str
    PaperlessBilling: str
    PaymentMethod: str
    MonthlyCharges: float
    TotalCharges: float
    
    # Outros (Alguns o modelo pode ter descartado, mas se pedir, entregamos)
    # No erro anterior, ele não pediu CreditScore/Geography/Age explicitamente na lista de missing,
    # mas o modelo Random Forest/XGB costuma usar. Vamos manter por segurança se estiverem no X_train.
    # Se o modelo foi treinado sem eles (devido ao drop), não fará mal enviar.
    # Mas baseado no seu erro, ele pediu EXPLICITAMENTE as colunas abaixo.

def generate_retention_plan(churn_prob, customer_profile):
    if not GEMINI_KEY:
        return "Plano indisponível (API Key não configurada)."
    
    try:
        client = genai.Client(api_key=GEMINI_KEY)
        
        prompt = f"""
        CONTEXTO: Cliente Telecom churn {churn_prob:.1%}. 
        PERFIL: {customer_profile}
        
        TAREFA: Aja como um Especialista de Sucesso do Cliente.
        Crie um plano tático de 3 ações imediatas para evitar o cancelamento.
        Foque em resolver dores ligadas ao tipo de contrato e serviço.
        Seja direto, comercial e empático. Responda em Português.
        TAREFA: Crie um plano de retenção de 3 pontos.
        REGRAS:
        1. NÃO faça introduções como "Como especialista...".
        2. Vá direto para a Ação 1, Ação 2, Ação 3.
        3. Seja curto e comercial.
        """
        
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,
            config=GenerateContentConfig(
                temperature=0.7,
                max_output_tokens=2048                
            )
        )
        return response.text
    except Exception as e:
        return f"Erro GenAI: {str(e)}"

class CustomerRequest(BaseModel):
    customer_id: str

def load_customers():
    try:
        return pd.read_excel(EXCEL_PATH)
    except Exception as e:
        raise RuntimeError(f"Erro ao ler planilha: {e}")

def get_customer_by_id(customer_id: str) -> dict:
    df = load_customers()

    customer = df[df["CustomerID"] == customer_id]

    if customer.empty:
        raise HTTPException(
            status_code=404,
            detail="CustomerID não encontrado"
        )

    return customer.iloc[0].to_dict()

@app.post("/predict")
def predict_churn(request: CustomerRequest):
    if pipeline is None:
        raise HTTPException(status_code=500, detail="Modelo ML não carregado.")

    try:
        customer = get_customer_by_id(request.customer_id)

        # Mapeamento EXATO para o nome das colunas que o modelo (pandas) espera.
        # Os nomes à esquerda DEVEM ser iguais aos do dataset de treino original.
        input_data = {
            'Gender': [customer['Gender']],
            'Senior Citizen': [customer['Senior Citizen']], # Espaço importante
            'Partner': [customer['Partner']],
            'Dependents': [customer['Dependents']],
            'Tenure Months': [customer['Tenure Months']],   # Espaço importante
            'Phone Service': [customer['Phone Service']],   # Espaço importante
            'Multiple Lines': [customer['Multiple Lines']], # Espaço importante
            'Internet Service': [customer['Internet Service']],
            'Online Security': [customer['Online Security']],
            'Online Backup': [customer['Online Backup']],
            'Device Protection': [customer['Device Protection']],
            'Tech Support': [customer['Tech Support']],
            'Streaming TV': [customer['Streaming TV']],
            'Streaming Movies': [customer['Streaming Movies']],
            'Contract': [customer['Contract']],
            'Paperless Billing': [customer['Paperless Billing']],
            'Payment Method': [customer['Payment Method']],
            'Monthly Charges': [customer['Monthly Charges']],
            'TotalCharges': [customer['Total Charges']]
        }
        
        df_input = pd.DataFrame(input_data)
        
        # Predição
        prediction = pipeline.predict(df_input)[0]
        probability = pipeline.predict_proba(df_input)[0][1]

        churn_risk = "BAIXO"
        retention_plan = "Cliente saudável."

        if probability > 0.50: 
            churn_risk = "ALTO" if probability > 0.75 else "MÉDIO"

            # Perfil mais rico para a IA
            profile_summary = (
                f"{customer['Gender']}, "
                f"Contrato {customer['Contract']}, "
                f"Internet {customer['Internet Service']}, "
                f"Pagamento {customer['Payment Method']}, "
                f"Gasto Mensal R${customer['Monthly Charges']}"
            )

            retention_plan = generate_retention_plan(probability, profile_summary)

        return {
            "prediction": int(prediction),
            "probability": float(round(probability, 4)),
            "risk_level": churn_risk,
            "retention_strategy": retention_plan
        }

    except Exception as e:
        print(f"ERRO: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "ok", "model_loaded": pipeline is not None}