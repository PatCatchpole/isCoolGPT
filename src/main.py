from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from .models import ChatRequest, ChatResponse
from .ai_client import ask_ai

# Cria a aplicação FastAPI
app = FastAPI(
    title="IsCoolGPT - Assistente de Estudos em Cloud",
    description="Tutor de Cloud Computing usando Gemini e FastAPI.",
    version="1.0.0",
)

# Monta a pasta de arquivos estáticos (onde está o index.html bonitinho)
# Caminho relativo à WORKDIR do container (/app), então precisa existir /app/static
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    """
    Página inicial - front-end estilo chat (index.html)
    """
    return FileResponse("static/index.html")


@app.get("/health")
def health():
    """
    Health check para ECS/ALB e monitoramento.
    """
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    """
    Endpoint principal do chat.
    Recebe question/topic/level e devolve a resposta da IA.
    """
    try:
        answer = ask_ai(
            question=request.question,
            topic=request.topic,
            level=request.level,
        )
        return ChatResponse(answer=answer)
    except Exception as exc:
        # Aqui você pode logar o erro com mais detalhe futuramente
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao consultar IA: {exc}",
        )

