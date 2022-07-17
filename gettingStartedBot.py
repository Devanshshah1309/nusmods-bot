import os
import telegram

TOKEN = os.getenv("TOKEN")

bot = telegram.Bot(TOKEN)
# print(bot.get_me()) # Verify that your bot credentials are correct

# print(bot.get_updates()[0]) # Run this after you have sent the /start command
chat = bot.get_updates()[0].message
chatId = chat.from_user.id

bot.send_message(text=f"Hi {chat.from_user.name}", chat_id=chatId)


    