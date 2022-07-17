from telegram import Update
from telegram.ext import ContextTypes
from api import getModulePrerequisite

async def prerequisite(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args == []:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Please enter a module code along with the describe command!\nFor example, /describe CS1101S")
        return
    module_code = (context.args[0]).upper()
    prerequisite = getModulePrerequisite(module_code)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"You have requested for the prerequisite of {module_code}. Here you go!")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=prerequisite)