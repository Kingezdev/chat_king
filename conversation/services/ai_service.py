import requests
from decouple import config
from .model_registery import get_model_config

HF_API_URL = config('HF_API_URL', default='https://router.huggingface.co/v1/chat/completions')
HF_API_KEY = config('HF_API_KEY', default='')

def chat_model(prompt: str, model_name: str):
    # get model configuration
    model_config = get_model_config(model_name)
    if not model_config:
        raise ValueError(f"Model '{model_name}' is not available.")
    
    payload = {
        "model": model_name,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": model_config.get("temperature", 0.7),
        "max_tokens": model_config.get("max_tokens", 2000)
    }

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(HF_API_URL, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return {
            "reply": data['choices'][0]['message']['content'],
            "model": model_name,
            "token_used": data.get("usage", {}).get("total_tokens", 0)
        }
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with AI service: {e}")
        return None