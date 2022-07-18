from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args == []:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Please enter a module code along with the check command!\nFor example, /check CS1101S")
        return
    options = []
    options.append(InlineKeyboardButton(text="Description", callback_data="description"))
    options.append(InlineKeyboardButton(text="Prerequisites", callback_data="prerequisite"))
    reply_markup = InlineKeyboardMarkup([options])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"What would you like to view for the module {context.args[0]}", reply_markup=reply_markup)