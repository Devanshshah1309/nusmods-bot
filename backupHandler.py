from telegram import Update
from telegram.ext import ContextTypes

async def backup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I couldn't recognise that command")