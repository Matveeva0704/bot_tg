import telebot 
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Куда я попал?")
	item2 = types.KeyboardButton("Информация")

	markup.add(item1, item2)

	bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот для студентов ВСГУТУ.".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def dialog(message):
	if message.chat.type == 'private':
		if message.text == 'Куда я попал?':
			bot.send_message(message.chat.id, "Вы находитесь в переписке с ботом от университета ВСГУТУ")
		elif message.text == 'Информация':

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton("Для студентов", callback_data='s1')
			item2 = types.InlineKeyboardButton("Для поступающих", callback_data='s0')

			markup.add(item1, item2)

			bot.send_message(message.chat.id, "Выберите", reply_markup=markup)
		else:
			bot.send_message(message.chat.id, 'Я не знаю что ответить 🤯')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	try:
		if call.message:
			if call.data == 's1':
				keyboard = types.InlineKeyboardMarkup()

				url_button = types.InlineKeyboardButton(text="Посмотреть расписание", url="https://portal.esstu.ru/raspisan.htm")

				keyboard.add(url_button)

				bot.send_message(call.message.chat.id, '🙂', reply_markup=keyboard)
			elif call.data == 's0':
				keyboard2 = types.InlineKeyboardMarkup()

				url_button2 = types.InlineKeyboardButton(text="Как поступить", url="https://www.esstu.ru/uportal/priem/scheme.htm")

				keyboard2.add(url_button2)

				bot.send_message(call.message.chat.id, '🙂', reply_markup=keyboard2)

	except Exception as e:
		print(repr(e))

# RUN
bot.polling(none_stop=True)
