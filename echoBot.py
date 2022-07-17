from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
import os
import echoHandler, startHandler

if __name__ == '__main__': # Ensures that this does not run when used to import
    TOKEN = os.getenv("TOKEN")
    BOT_NAME = os.getenv("BOT_NAME")

    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', startHandler)

    # filters are used to determine the kind of updates/messages you want to reply to
    # filters are combined using bitwise operators instead of logical operators
    echo_handler = MessageHandler(filters=filters.TEXT, callback=echoHandler)
    
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    
    application.run_polling() # To ensure that you run the bot until you manually close it
