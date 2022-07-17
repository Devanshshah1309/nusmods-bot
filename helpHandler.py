from telegram import Update
from telegram.ext import ContextTypes
from api import getModulePrerequisite

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    HELP_MESSAGE = f"Hi {update.effective_user.first_name}! Hope you're doing well!\nThese are the following commands you can use:\n1. /describe <module_code>\n2. /prerequisite <module_code>\n3. /check <module_code>"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=HELP_MESSAGE)