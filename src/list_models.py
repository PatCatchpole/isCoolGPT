import os
import google.generativeai as genai

api_key = os.getenv("AI_API_KEY")
if not api_key:
    raise RuntimeError("Defina a variável de ambiente AI_API_KEY antes de rodar isso.")

genai.configure(api_key=api_key)

print("Modelos disponíveis:")
for m in genai.list_models():
    # Só mostrar modelos que suportam generateContent
    if "generateContent" in getattr(m, "supported_generation_methods", []):
        print("-", m.name)
