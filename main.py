import telebot
from info import hobby_list
from info import special_list
from config import token


bot = telebot.TeleBot(token=token)
chat_id = 5050226393


@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.reply_to(message, f"Привет {message.from_user.first_name}, я Тони Старк, жми /help чтобы начать со мной общение")
    photo = open("C:\\Users\lenovo\Downloads\\tryToni.jpg", 'rb')
    bot.send_photo(chat_id, photo)

@bot.message_handler(commands=['help'])
def help_msg(message):
    bot.reply_to(message, "Могу рассказать вам о себе!\n"
                          "Можете спросить кто я вообще такой? - /who - да кто ты такой без своего костюма?\n"
                          "А могу вам мемы прислать по марвел - /memes - пришли ка мне мемчики\n"
                          "А могу и рассказать о себе подробненько - /about - расскажи о себе\n"
                          "Чтобы попрощаться, можешь написать 'пока', 'прощай' или 'до свидания'")

@bot.message_handler(commands=['who'])
def heh_msg(message):
    bot.reply_to(message, "Гений, миллиардер, плейбол, филантроп.")
    photo = open("C:\\Users\lenovo\Downloads\\tony.jpg", 'rb')
    bot.send_photo(chat_id, photo)

@bot.message_handler(commands=['memes'])
def start_msg(message):
    bot.reply_to(message, "Уан Секонд")
    photo = open("C:\\Users\lenovo\Downloads\\Tony_meme.jpg", 'rb')
    bot.send_photo(chat_id, photo)


@bot.message_handler(commands = ['about'])
def about_msg(message):
    for key, value in hobby_list():
        bot.reply_to(f"{key} - {value['hobby']}")

@bot.message_handler(content_types = ['text'])
def goodbye_msg(message):
    if message == 'пока' or 'прощай' or 'до свидания':
        bot.send_message(message.chat.id, "Всего хорошего, бывай")

@bot.message_handler()
def send_text(message):
    bot.send_message(message.chat.id, 'Чтобы мы поговрили как надо, следуй инструкцийм которые я присылаю')
    bot.send_message(message.chat.id, 'введи что то что я умею распозновать, а то увы, наше общение здесь и закончится ')

bot.polling()