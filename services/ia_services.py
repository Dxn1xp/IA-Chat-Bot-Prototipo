import os
import requests
from dotenv import load_dotenv

load_dotenv("api.env") #Carrega arquivo

class IAService:
    """
    Serviço de integração com o modelo de IA via Groq.
    """

    MODELO = "llama-3.3-70b-versatile"
    MAX_TOKENS = 1024
    API_URL = os.getenv("API_URL", "./")
    API_KEY = os.getenv("API_KEY", "")

    @classmethod
    def gerar_resposta(cls, mensagem_usuario: str) -> str:
        headers = {
            "Authorization": f"Bearer {cls.API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": cls.MODELO,
            "messages": [
                {"role": "system", "content": "Você é um assistente útil e amigável."},
                {"role": "user", "content": mensagem_usuario}
            ],
            "max_tokens": cls.MAX_TOKENS
        }

        response = requests.post(cls.API_URL, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise Exception(f"Erro na chamada da API: {response.status_code} - {response.text}")
        