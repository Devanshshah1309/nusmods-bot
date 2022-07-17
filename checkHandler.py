from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from api import getModuleDescription

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args == []:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Please enter a module code along with the check command!\nFor example, /check CS1101S")
        return
    options = []
    options.append(InlineKeyboardButton(text="Description", callback_data="Description"))
    reply_markup = InlineKeyboardMarkup([options])
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Choose one of the following actions", reply_markup=reply_markup)