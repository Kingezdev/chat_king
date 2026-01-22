# conversation models registry

FREE_MODELS = {
    "meta-llama/Llama-3.3-70B-Instruct":{
        "provider": "Groq",
        "description":"Llama-3.3-70B-Instruct is multilingual large language model (LLM), an instruction tuned generative model in 70B (text in/text out). The Llama 3.3 instruction tuned text only model is optimized for multilingual dialogue use cases and outperforms many of the available open source and closed chat models on common industry benchmarks",
        "max_tokens": 2000,
        "temperature": 0.7
    }
}

def get_free_models():
    return FREE_MODELS

def get_model_config(model_name: str):
    return FREE_MODELS.get(model_name, None)