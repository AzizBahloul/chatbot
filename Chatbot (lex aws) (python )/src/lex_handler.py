import boto3
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class LexHandler:
    def __init__(self):
        self.client = boto3.client('lex-runtime', region_name=os.getenv('AWS_REGION'))
        self.bot_name = os.getenv('LEX_BOT_NAME')
        self.bot_alias = os.getenv('LEX_BOT_ALIAS')
        self.user_id = 'user123'  # A unique identifier for the user

    def send_message(self, message):
        response = self.client.post_text(
            botName=self.bot_name,
            botAlias=self.bot_alias,
            userId=self.user_id,
            inputText=message
        )
        return response
