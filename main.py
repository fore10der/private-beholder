from beholder import start_handler, validate_handler
from bot import dispatcher, updater

dispatcher.add_handler(start_handler)
dispatcher.add_handler(validate_handler)

updater.start_polling()