import telebot
token = "1310155222:AAGRUfmrIomT9gPJgRCuto_5IYLCI1PhgOg"
bot = telebot.TeleBot(token)
adminchatid = "346037244" #look in database file

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
            joinedFile.write(str(message.chat.id) + "\n")
            joinedUsers.add(str(message.chat.id))
    except TypeError:
        if not str(message.chat.id) in joinedUsers:
            joinedFile = open("db.txt", "a")
            joinedFile.write(str(message.chat.id) + "\n")
            joinedUsers.add(str(message.chat.id))



@bot.message_handler(commands=['special'])
def mess(message):
    f = open("db.txt", "rb")
    bot.send_document(chat_id=adminchatid, data=f)

if __name__ == '__main__':
    bot.polling(none_stop=True)
