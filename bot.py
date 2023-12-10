import telebot
token = "6306091019:AAFuMsyIDct0_9FZCyN_YUT3FHl8cdQLBy0"

bot = telebot.TeleBot(token=token)
chat_id = 5050226393
@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.reply_to(message, "Я Тони Старк, и да, я говорю по вашему.")

bot.send_message(chat_id,"Я Тони Старк!")
bot.polling()