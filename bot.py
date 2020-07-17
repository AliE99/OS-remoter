import telebot

# this is not the real token duo to security issues
TOKEN = ""
bot = telebot.TeleBot(TOKEN)

def getFile(filename):
    file = open(filename, "r+")
    return file.read()



def putFile(filename, content):
    file = open(filename, "w+")
    file.write(content)
    file.close()



@bot.message_handler(content_types=['text'])
def botMain(response):
    userText = response.text
    userChatId = response.chat.id
    userUsername = response.chat.username
    userFirstName = response.chat.first_name
    userLastName = response.from_user.last_name
    admins = getFile("admins.txt").splitlines()
    if userUsername in admins:
        bot.send_message(userChatId, "Hey Buddy !")
    else:
        bot.send_message(userChatId, "Go Fuck yourself")



bot.polling(True)



