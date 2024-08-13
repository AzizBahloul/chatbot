import os
from dotenv import load_dotenv

load_dotenv()

LEX_BOT_NAME = os.getenv('LEX_BOT_NAME')
LEX_BOT_ALIAS = os.getenv('LEX_BOT_ALIAS')
AWS_REGION = os.getenv('AWS_REGION')
USE_LEX_DEFAULT = os.getenv('USE_LEX_DEFAULT', 'True').lower() in ['true', '1', 't', 'y', 'yes']
