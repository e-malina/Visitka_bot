import telebot
from info import hobby_list
from info import special_list
from config import token


bot = telebot.TeleBot(token=token)
chat_id = 5050226393


@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.reply_to(message, f"Привет {message.from_user.first_name}, я Тони Старк жми /help чтобы начать со мной общение")
    photo = open("C:/Users/lenovo/Downloads/tryToni.jpg", 'rb')
    bot.send_photo(chat_id, photo)

@bot.message_handler(commands=['help'])
def help_msg(message):
    bot.reply_to(message, "Могу рассказать вам о себе!\n"
                          "Можешь спросить кто я вообще такой? - /who - 'да кто ты такой без своего костюма'?\n"
                          "А могу и мемы про марвел прислать - /memes - 'пришли ка мне мемчики'\n"
                          "А могу и рассказать о своих хобби - /about - 'расскажи о себе!'\n"
                          "Жми /details чтобы узнать обо мне чуточку больше))"
                          "Чтобы попрощаться, можешь написать 'пока' или 'прощай'")

@bot.message_handler(commands=['who'])
def heh_msg(message):
    bot.reply_to(message, "Гений, миллиардер, плейбол, филантроп.")
    photo = open("C:/Users/lenovo/Downloads/tony.jpg", 'rb')
    bot.send_photo(chat_id, photo)

@bot.message_handler(commands=['memes'])
def meme_msg(message):
    bot.reply_to(message, "Уан Секонд")
    photo = open("C:/Users/lenovo/Downloads/Tony_meme.jpg", 'rb')
    bot.send_photo(chat_id, photo)
    bot.reply_to(message, "Жми /more чтобы я прислал еще один мемчик")

@bot.message_handler(commands=['more'])
def more_msg(message):
    photo1 = open("C:/Users/lenovo/Downloads/meme2.jpg", 'rb')
    bot.send_photo(chat_id, photo1)


@bot.message_handler(commands = ['about'])
def about_msg(message):
    for key, value in hobby_list.items():
        bot.reply_to(message, f"{key}. {value['hobby']} - {value['description']}")

@bot.message_handler(commands = ['details'])
def about_msg(message):
    for key, value in special_list.items():
        bot.reply_to(message, f"{key} - {value}")

@bot.message_handler(content_types = ['text'])
def goodbye_msg(message):
    if message.text.lower() == 'пока' or message.text.lower() == 'прощай' or message.text.lower() == 'до свидания':
        bot.send_message(message.chat.id, "Всего хорошего, бывай")

@bot.message_handler()
def send_text(message):
    bot.send_message(message.chat.id, 'Чтобы мы поговрили как надо, следуй инструкциям которые я присылаю')
    bot.send_message(message.chat.id, 'введи что то что я умею распозновать, а то увы, наше общение здесь и закончится ')




bot.polling()