import telebot
token = ""
bot = telebot.TeleBot(token)


joinedFile = open("C:\db\db.txt", "r")
joinedUsers = set ()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()

@bot.message_handler(commands=['start'])
def startJoin(message):
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("C:\db\db.txt", "a")
        joinedFile.write(str(message.chat.id) + " " + message.from_user.username + "\n")
        joinedUsers.add(message.chat.id)

@bot.message_handler(commands=['special'])
def mess(message):
    for user in joinedUsers:
        bot.send_message(user, message.text[message.text.find(' '):])




if __name__ == '__main__':
    bot.polling(none_stop=True)
