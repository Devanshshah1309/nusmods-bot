from email.message import Message
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
import os
TOKEN = os.getenv("TOKEN")
BOT_NAME = os.getenv("BOT_NAME")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    update.message.text
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hi {update.effective_user.first_name}! Thanks for using {BOT_NAME}\nWhat would you like to do today?")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

if __name__ == '__main__': # Ensures that this does not run when used to import
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler('start', start)
    # filters are used to determine the kind of updates/messages you want to reply to
    # filters are combined using bitwise operators instead of logical operators
    echo_handler = MessageHandler(filters=filters.TEXT, callback=echo)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.run_polling() # To ensure that you run the bot until you manually close it
