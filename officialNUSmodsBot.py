from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from backupHandler import backup
from describeHandler import describe
from startHandler import start

import os

if __name__ == '__main__': # Ensures that this does not run when used to import
    TOKEN = os.getenv("TOKEN")
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    describe_handler = CommandHandler('describe', describe)
    backup_handler = MessageHandler(filters.COMMAND, backup)

    # Order of adding handlers matters! It indicates the order of precedence
    application.add_handler(start_handler)
    application.add_handler(describe_handler)
    application.add_handler(backup_handler)
    application.run_polling() # To ensure that you run the bot until you manually close it
