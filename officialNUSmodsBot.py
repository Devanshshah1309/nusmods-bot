from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters
from backupHandler import backup
from describeHandler import describe
from startHandler import start
from checkHandler import check
from callbackHandler import callback
from helpHandler import help
from prerequisiteHandler import prerequisite

import os

if __name__ == '__main__': # Ensures that this does not run when used to import
    TOKEN = os.getenv("TOKEN")
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    describe_handler = CommandHandler('describe', describe)
    check_handler = CommandHandler('check', check)
    backup_handler = MessageHandler(filters.COMMAND, backup)
    callback_handler = CallbackQueryHandler(callback)
    help_handler = CommandHandler('help', help)
    prerequisite_handler = CommandHandler('prerequisite', prerequisite)

    # Order of adding handlers matters! It indicates the order of precedence
    application.add_handler(start_handler)
    application.add_handler(describe_handler)
    application.add_handler(check_handler)
    application.add_handler(callback_handler)
    application.add_handler(prerequisite_handler)
    application.add_handler(help_handler)
    
    application.add_handler(backup_handler)
    application.run_polling() # To ensure that you run the bot until you manually close it
