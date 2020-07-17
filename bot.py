import telebot

# this is not the real token duo to security issues
TOKEN = "token"
bot = telebot.TeleBot(TOKEN)

bot.polling(True)
