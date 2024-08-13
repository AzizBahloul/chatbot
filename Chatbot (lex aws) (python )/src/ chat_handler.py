from typing import Optional
from .lex_handler import LexHandler

class ChatHandler:
    def __init__(self):
        self.lex_handler = LexHandler()

    def handle_message(self, message: str, use_lex: Optional[bool] = True):
        if use_lex:
            return self.lex_handler.send_message(message)
        else:
            return {"message": f"Echo: {message}"}
