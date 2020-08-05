import telebot
token = "1310155222:AAGRUfmrIomT9gPJgRCuto_5IYLCI1PhgOg"
bot = telebot.TeleBot(token)


joinedFile = open("db.txt", "r")
joinedUsers = set ()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()

@bot.message_handler(commands=['start'])
def startJoin(message):
    try:
        if not str(message.chat.id) in joinedUsers:
            joinedFile = open("db.txt", "a")
            joinedFile.write(str(message.chat.id) + " " + message.from_user.username + "\n")
            joinedUsers.add(str(message.chat.id))
    except TypeError:
        if not str(message.chat.id) in joinedUsers:
            joinedFile = open("db.txt", "a")
            joinedFile.write(str(message.chat.id) + "\n")
            joinedUsers.add(str(message.chat.id))
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Сhoose the currency you want to convert to", reply_markup=keyboard())

@bot.message_handler(commands=['special'])
def mess(message):
    for user in joinedUsers:
        bot.send_message(user, message.text[message.text.find(' '):])




if __name__ == '__main__':
    bot.polling(none_stop=True)
