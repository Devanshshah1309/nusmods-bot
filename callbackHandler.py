from telegram import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from describeHandler import describe
from prerequisiteHandler import prerequisite

async def callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # this is only called when a button is clicked
    module_code = update.callback_query.message.text.split()[-1]
    if update.callback_query.data == "description":
        describe(module_code)
    elif update.callback_query.data == "prerequisite":
        prerequisite(module_code)
