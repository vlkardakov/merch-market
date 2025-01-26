import telebot
import time
import os

TOKEN = '7844571279:AAHiaKLNOQZeUkOVlfM7k_mUzARoEDCNNu4'
bot = telebot.TeleBot(TOKEN)

print("imported")

def pithon(code):
    global result
    try:
        local_vars = {}
        exec(code, {}, local_vars)
        return local_vars.get('result')
    except:
        pass


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, message.chat.id)
    bot.register_next_step_handler(message, process_user_message)

therds = []

anscounter = 0


def process_user_message(message):
    print(f"{message.text=}")
    t = message.text
    t = input(f"Пользователь: {t}\n")
    bot.reply_to(message, t)
    bot.register_next_step_handler(message, process_user_message)


if __name__ == "__main__":
    bot.polling()