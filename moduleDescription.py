import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
from echo import start, TOKEN

URL = "http://api.nusmods.com/v2/2022-2023/modules/"

def getModuleDescription(module_code: str):
    r = requests.get(f"{URL}{module_code}.json")
    data = r.json()
    return data['description']

# arguments passed to a command are sent the command handler via context.args
async def describe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args == []:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Please enter a module code along with the describe command!\nFor example, /describe CS1101S")
        return
    module_code = context.args[0]
    description = getModuleDescription(module_code)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"You have requested for the module description of {module_code}. Here you go!")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=description)

if __name__ == '__main__': # Ensures that this does not run when used to import
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler('start', start)
    describe_handler = CommandHandler('describe', describe)
    application.add_handler(start_handler)
    application.add_handler(describe_handler)
    application.run_polling() # To ensure that you run the bot until you manually close it
