import os
import google.generativeai as genai

AI_API_KEY = os.getenv("AI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL","gemini-2.5-flash")  # default aqui tanto faz, vamos passar por env

if not AI_API_KEY:
    raise RuntimeError("AI_API_KEY não configurada. Defina a variável de ambiente AI_API_KEY.")

genai.configure(api_key=AI_API_KEY)


def ask_ai(question: str, topic: str | None = None, level: str | None = None) -> str:
    system_prompt = "Você é um tutor de Cloud Computing que explica tudo de forma simples e didática."
    if topic:
        system_prompt += f" Foque no tema: {topic}."
    if level:
        system_prompt += f" O nível do aluno é: {level}."

    contents = [
        {"role": "user", "parts": system_prompt},
        {"role": "user", "parts": question},
    ]

    model = genai.GenerativeModel(GEMINI_MODEL)
    response = model.generate_content(contents)

    if hasattr(response, "text") and response.text:
        return response.text.strip()

    return "Não consegui gerar uma resposta no momento. Tente novamente mais tarde."
