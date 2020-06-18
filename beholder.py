from dotenv import load_dotenv

load_dotenv()
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler
from telegram.update import Update
import os

# START VIEW
CONDITIONAL_CHANNEL_URL = os.getenv('CONDITIONAL_CHANNEL_URL')
CONDITIONAL_CHANNEL_ID = '-100' + str(os.getenv('CONDITIONAL_CHANNEL_ID'))
PRIVATE_CHANNEL_URL = os.getenv('PRIVATE_CHANNEL_URL')

START_BUTTONS = [[InlineKeyboardButton("Подписаться", url=CONDITIONAL_CHANNEL_URL)],
                 [InlineKeyboardButton("Проверить подписку", callback_data="validate")]]

START_MARKUP = InlineKeyboardMarkup(START_BUTTONS)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Подпишись, чтобы посмотреть продолжение!", reply_markup=START_MARKUP)


# VALIDATE VIEW

VALIDATE_BUTTONS = [[InlineKeyboardButton("В приватный канал", url=PRIVATE_CHANNEL_URL)]]
VALIDATE_MARKUP = InlineKeyboardMarkup(VALIDATE_BUTTONS)


def validate(update: Update, context: CallbackContext):
    update = update.callback_query
    user = context.bot.get_chat_member(chat_id=CONDITIONAL_CHANNEL_ID, user_id=update.message.chat_id)
    if user and user.status != 'left':
        context.bot.edit_message_text(
            chat_id=update.message.chat_id,
            message_id=update.message.message_id,
            text='Ты подписался!\nСмотри продолжение в приватном канале',
            reply_markup=VALIDATE_MARKUP
        )
        return
    context.bot.edit_message_text(
        chat_id=update.message.chat_id,
        message_id=update.message.message_id,
        text='Ты не подписался.\nПодпишись, чтобы посмотреть продолжение!',
        reply_markup=START_MARKUP
    )


start_handler = CommandHandler('start', start)
validate_handler = CallbackQueryHandler(validate, 'validate')
