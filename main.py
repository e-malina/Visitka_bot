import telebot
token = "6306091019:AAFuMsyIDct0_9FZCyN_YUT3FHl8cdQLBy0"

bot = telebot.TeleBot(token=token)
chat_id = 5050226393


@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.reply_to(message, "Я Тони Старк, пиши /help чтобы начать со мной общение")
    photo = open("C:\\Users\lenovo\Downloads\\tryToni.jpg", 'rb')
    bot.send_photo(chat_id, photo)

@bot.message_handler(commands=['help'])
def help_msg(message):
    bot.reply_to(message, "Могу рассказать вам о себе!\n"
                          "Можете спросить кто я вообще такой? - /who - да кто ты такой без своего костюма?\n"
                          "А могу вам мемы прислать по марвел - /memes - пришли ка мне мемчики\n"
                          "А могу и рассказать о себе подробненько - расскажи о себе")

@bot.message_handler(commands=['who'])
def heh_msg(message):
    bot.reply_to(message, "Гений, миллиардер, плейбол, филантроп.")
    photo = open("C:\\Users\lenovo\Downloads\\tony.jpg", 'rb')
    bot.send_photo(chat_id, photo)

@bot.message_handler(commands=['/memes'])
def start_msg(message):
    bot.reply_to(message, "Уан Секонд")
    photo = open("C:\\Users\lenovo\Downloads\\Tony_meme.jpg", 'rb')
    bot.send_photo(chat_id, photo)

@bot.message_handler()
def send_text(message):
    bot.send_message(message.chat.id, 'Чтобы мы поговрили как надо, советую следовать инструкцийм которые я присылаю')
    bot.send_message(message.chat.id, 'введи что то что я умею распозновать, а то увы, наше общение здесь и закончится ')

bot.polling()