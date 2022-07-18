from telegram import Update
from telegram.ext import ContextTypes
import os

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    BOT_NAME = os.getenv("BOT_NAME")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hi {update.effective_user.first_name}! Thanks for using {BOT_NAME}\nWhat would you like to do today?")