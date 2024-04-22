import json
import telebot
import requests
# import sqlite3
# import webbrowser
# from telebot import types

bot = telebot.TeleBot('7064640921:AAFUPlUzNWRY79CovZiSrJ55trH1evAic5E')
api = 'e6e7347b0b7c998aa4474e708f787ea0'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello, what's up? Write a name of the city")


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    respond = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
    if respond.status_code == 200:
        data = json.loads(respond.text)
        temp = data['main']['temp']
        bot.reply_to(message, f"The weather in {data['name']} is {temp}°C")

        image = 'warm.png' if int(temp) >= 15.0 else 'cold.jpg'
        file = open(image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, "Ooops, I couldn't find this city")


# name = None

# @bot.message_handler(commands=['start'])
# def start(message):
#     conn = sqlite3.connect('db.sql')
#     cur = conn.cursor()

#     cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
#     conn.commit()
#     cur.close()
#     conn.close()

#     bot.send_message(message.chat.id, 'Hi, please register first. Input your name')
#     bot.register_next_step_handler(message, user_name)


# def user_name(message):
#     global name
#     name = message.text.strip()
#     bot.send_message(message.chat.id, 'Create a password')
#     bot.register_next_step_handler(message, user_pass)


# def user_pass(message):
#     password = message.text.strip()

#     conn = sqlite3.connect('db.sql')
#     cur = conn.cursor()

#     cur.execute("INSERT INTO users (name, pass) VALUES('%s', '%s')" % (name, password))
#     conn.commit()
#     cur.close()
#     conn.close()

#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Users', callback_data='users'))
#     bot.send_message(message.chat.id, 'You have been successfully registered', reply_markup=markup)


# @bot.callback_query_handler(func=lambda call: True)
# def callback(call):
    
#     conn = sqlite3.connect('db.sql')
#     cur = conn.cursor()

#     cur.execute("SELECT * FROM users")
#     users = cur.fetchall()

#     info = ''
#     for i in users:
#         info += f'Name: {i[1]}, password: {i[2]}\n'

#     cur.close()
#     conn.close()

#     bot.send_message(call.message.chat.id, info)


# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     button1 = types.KeyboardButton('Visit the site')
#     button2 = types.KeyboardButton('Delete the photo')
#     button3 = types.KeyboardButton('Edit the photo')
#     markup.row(button1)
#     markup.row(button2, button3)
#     file = open('eren.jpg', 'rb')
#     bot.send_photo(message.chat.id, file, reply_markup=markup)
#     # bot.send_message(message.chat.id, 'Hello', reply_markup=markup)
#     bot.register_next_step_handler(message, on_click)


# def on_click(message):
#     if message.text == 'Visit the site':
#         bot.send_message(message.chat.id, 'Website is open')
#     elif message.text == 'Delete the photo':
#         bot.send_message(message.chat.id, 'Phote has been deleted')


# @bot.message_handler(commands=['site', 'website'])
# def site(message):
#     webbrowser.open('https://youtu.be/WIRK_pGdIdA?si=P7eiipHKzlApy15x')


# @bot.message_handler(commands=['start'])
# def start(message):
#     bot.send_message(message.chat.id, f"Welcome, {message.from_user.first_name} {message.from_user.last_name if message.from_user.last_name != None else ''}\U0001F921")


# @bot.message_handler(commands=['help'])
# def start(message):
#     bot.send_message(message.chat.id, '<b>What do you wnat to know,</b> <i>clown\U0001F921?</i>', parse_mode='html')


# @bot.message_handler()
# def info(message):
#     if message.text.lower() == 'hello':
#         bot.send_message(message.chat.id, f"Welcome, {message.from_user.first_name} {message.from_user.last_name if message.from_user.last_name != None else ''}\U0001F921")
#     elif message.text.lower() == 'id':
#         bot.reply_to(message, f"ID: {message.from_user.id}")


# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup()
#     button1 = types.InlineKeyboardButton('Visit the site', url='https://youtube.com')
#     button2 = types.InlineKeyboardButton('Delete the photo', callback_data='delete')
#     button3 = types.InlineKeyboardButton('Edit the photo', callback_data='edit')
#     markup.row(button1)
#     markup.row(button2, button3)

#     bot.reply_to(message, 'An average cringy photo\U0001F921', reply_markup=markup)


# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == 'delete':
#         bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
#     elif callback.data == 'edit':
#         bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)



bot.polling(non_stop=True)