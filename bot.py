import os
from telegram.ext import Updater, Dispatcher
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')
PROXY_URL = os.getenv('PROXY_URL')
updater = Updater(token=TOKEN, use_context=True, request_kwargs={
    'proxy_url': PROXY_URL
})
dispatcher: Dispatcher = updater.dispatcher
