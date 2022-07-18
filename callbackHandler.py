from telegram import Update
from telegram.ext import ContextTypes
from api import getModuleDescription, getModulePrerequisite

async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # this is only called when a button is clicked
    module_code = update.callback_query.message.text.split()[-1]
    text = "Sorry, invalid callback query!"
    if update.callback_query.data == "description":
        text = getModuleDescription(module_code)
    elif update.callback_query.data == "prerequisite":
        text = getModulePrerequisite(module_code)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
