"""
latin to krill 

@author: rashidovj
"""

# from transliterate import to_latin , to_cyrillic

# matn = input ('Istalgan matn kiriting \n')

# if matn.isascii() :  
#     print(to_cyrillic(matn))

# else :
#     print(to_latin(matn))

import telebot
from transliterate import to_cyrillic, to_latin

TOKEN = "6355325479:AAGZX0J7kjU4Uhk68skNv549_KponhtPu3U"  # <-- maxfiy kodni yozish uchun 
bot = telebot.TeleBot(token=TOKEN)

# \start komandasi uchun mas'ul funksiya
@bot.message_handler(commands=["start"])
def send_welcome(message):
    username = (
        message.from_user.username
    )  # Bu usul bilan foydalanuvchi nomini olishimiz mumkin
    xabar = f"Assalom alaykum, {username} Kirill-Lotin-Kirill botiga xush kelibsiz!"
    xabar += "\nMatningizni yuboring."
    bot.reply_to(message, xabar)


# matnlar uchun mas'ul funksiya
@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))


bot.polling()
