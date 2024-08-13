from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .chat_handler import ChatHandler

app = FastAPI()
chat_handler = ChatHandler()

class ChatRequest(BaseModel):
    message: str
    use_lex: bool = True  # Whether to use Lex or not

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = chat_handler.handle_message(request.message, request.use_lex)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
