import telebot
from telebot import types

# Создание экземпляра бота
bot = telebot.TeleBot('5907538555:AAEgEcC5V1Pf5dC76jS269OpLP3_9dFiU3M')


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def startMessage(message):
    bot.send_message(message.chat.id, "Приветствую!\nЭто твой бот-гид по Дагестану!\n"
                                      "Здесь ты сможешь найти все интересующие тебя места и узнать о них подробнее.")
    sendMenu(message)


def sendMenu(message):
    global stage
    stage = 0
    city_names = ['Махачкала', 'Дербент', 'Избербаш']
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = []

    for city_name in city_names:
        button = types.InlineKeyboardButton(city_name, callback_data=city_name)
        buttons.append(button)
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, 'Выберите город', reply_markup=keyboard)


# Обработчик обратных вызовов кнопок
@bot.callback_query_handler(func=lambda call: True)
def handleCallbackQuery(call):
    global city
    if call.data == 'beach':
        sendBeach(call.message)
        messageId = call.message.message_id
        bot.delete_message(call.message.chat.id, messageId)
    elif call.data == "Городской пляж":
        name = "Городской пляж"
        sendInfo(call.message, name)
        messageId = call.message.message_id
        bot.delete_message(call.message.chat.id, messageId)
    elif call.data == "Оазис":
        name = "Оазис"
        sendInfo(call.message, name)
        messageId = call.message.message_id
        bot.delete_message(call.message.chat.id, messageId)
    elif call.data == "Березка":
        name = "Березка"
        sendInfo(call.message, name)
        messageId = call.message.message_id
        bot.delete_message(call.message.chat.id, messageId)
    elif call.data == 'culture':
        sendCulture(call.message)
        messageId = call.message.message_id
        bot.delete_message(call.message.chat.id, messageId)
    elif call.data == "Памятник Русской учительнице":
        name = "Памятник Русской учительнице"
        sendInfo(call.message, name)
        messageId = call.message.message_id
        bot.delete_message(call.message.chat.id, messageId)
    elif call.data == "Тарки-Тау":
        name = "Тарки-Тау"
        sendInfo(call.message, name)
        messageId = call.message.message_id
        bot.delete_message(call.message.chat.id, messageId)
    elif call.data == "Сарыкумский бархан":
        name = "Сарыкумский бархан"
        sendInfo(call.message, name)
        messageId = call.message.message_id
        bot.delete_message(call.message.chat.id, messageId)
    elif call.data == 'back':
        if stage == 1:
            sendMenu(call.message)
            messageId = call.message.message_id
            bot.delete_message(call.message.chat.id, messageId)
        elif stage == 2:
            sendSubMenu(call.message)
            messageId = call.message.message_id
            bot.delete_message(call.message.chat.id, messageId)
        elif stage == 3:
            if isBeach:
                sendBeach(call.message)
                messageId = call.message.message_id
                bot.delete_message(call.message.chat.id, messageId)
            else:
                sendCulture(call.message)
                messageId = call.message.message_id
                bot.delete_message(call.message.chat.id, messageId)
    elif call.data == 'Махачкала':
        city = "Махачкала"
        citySubMenu(call)
    elif call.data == 'Дербент':
        city = "Дербент"
        citySubMenu(call)
    elif call.data == 'Избербаш':
        city = "Избербаш"
        citySubMenu(call)


def citySubMenu(call):
    global city, city_check
    sendSubMenu(call.message)
    messageId = call.message.message_id
    bot.delete_message(call.message.chat.id, messageId)
    city_check = city
    if city[-1] in "аоеу":
        city = city[0:-1] + "е"
    else:
        city = city + "е"


beachArrayM = [["Городской пляж", "12.2 км", "Городской пляж Махачкалы является излюбленным местом отдыха как для "
                                             "горожан, так и для туристов, посещающих столицу Дагестана. Несмотря на то, "
                                             "что республика несколько лет не может решить проблему загрязнения моря, "
                                             "и купаться в Каспии у берега запрещено, в жаркие дни рекреационная зона "
                                             "заполняется до отказа. Соленый, насыщенный йодом воздух напоминает о "
                                             "курорте, а красота пейзажа умиротворяет и без погружения в воду.",
                "https://welcomedagestan.ru/wp-content/uploads/2018/07/5O6A2613.jpg"],
               ["Оазис", "14.1 км", "Один из наиболее известных пляжей Махачкалы. Расположен на выезде из столицы "
                                    "республики Дагестан.",
                "https://avatars.mds.yandex.net/get-altay/5482460/2a0000017d6ec4a5b6e8ebd32615a08162d2/orig"],
               ["Березка",
                "17.8 км",
                "Большой и чистый песчаный пляж «Березка» в Махачкале считается детским. Справа и слева он защищен двумя длинными насыпями из крупных валунов и больше похож на тихую заводь, где не бывает высоких волн. Прохладная по утрам вода во второй половине дня хорошо прогревается. Дно ровное, практически без камней, особенно в правой половине пляжа. Заход в воду пологий — глубина начинается только в 100 м от берега.",
                "https://img.tourister.ru/files/2/8/4/7/6/8/0/0/original.jpg"]]
cultureArrayM = [["Памятник Русской учительнице", '2.23км', 'Данный памятник — это символ жертвенности и патриотизма '
                                                            'русских  педагогов которых направляли на работу в учебные '
                                                            'заведения Дагестана.',
                  "https://icdn.lenta.ru/images/2023/05/11/12/20230511123200369/pwa_vertical_1024_84988fb2527b34012882e45fdf919b15.jpg"],
                 ["Тарки-Тау", '4.5 км', 'Тарки-Тау – '
                                         'огромная '
                                         'столообразная возвышенность, которая тянется вдоль Махачкалы параллельно морю. Ее длина достигает 12 км, а ширина 4-5 км. Она расположена над селом Агачаул. Высшая точка плато – вершина Тиктюбе, высотой 725 метра',
                  "https://upload.wikimedia.org/wikipedia/commons/2/26/%D0%92%D0%B8%D0%B4_%D0%BD%D0%B0_%D0%B3%D0%BE%D1%80%D1%83_%D0%A2%D0%B0%D1%80%D0%BA%D0%B8-%D0%A2%D0%B0%D1%83_%D1%81_%D1%81%D0%B5%D0%B2%D0%B5%D1%80%D0%B0.jpg"],
                 ["Сарыкумский бархан", '21 км', 'Бархан Сарыкум или, как его еще называют, Сарыкумский бархан — это '
                                                 'крупнейший песчаный бархан в Европе. Его протяженность - 12 км, '
                                                 'а ширина около 4 км. Высота песка более 250 метров.',
                  "https://caspian.travel/upload/places/barhan-sarykum/5667fgr.jpg"]]


def sendInfo(message, name):
    global stage
    stage = 3
    buttonBack = types.InlineKeyboardButton('Назад', callback_data='back')
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(buttonBack)
    for i in range(len(arr)):
        if name == arr[i][0]:
            bot.send_message(message.chat.id, f"{arr[i][0]}\n{arr[i][2]} \n{arr[i][3]}\n"
                                              f"Расстояние до места - {arr[i][1]}",
                             reply_markup=keyboard)


def sendBeach(message):
    global stage
    global name
    global arr
    global isBeach
    isBeach = True
    stage = 2
    buttonBack = types.InlineKeyboardButton('Назад', callback_data='back')
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = []
    arr = []
    if city_check == "Махачкала":
        arr = beachArrayM
    for i in range(len(arr)):
        name = arr[i][0]
        button = types.InlineKeyboardButton(name, callback_data=name)
        buttons.append(button)
    keyboard.add(*buttons)
    keyboard.add(buttonBack)
    bot.send_message(message.chat.id, f"Пляжи в {city}", reply_markup=keyboard)


def sendCulture(message):
    global isBeach
    global stage
    global name
    global arr
    isBeach = False
    stage = 2
    buttonBack = types.InlineKeyboardButton('Назад', callback_data='back')
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = []
    arr = []
    if city_check == "Махачкала":
        arr = cultureArrayM
    for i in range(len(arr)):
        name = arr[i][0]
        button = types.InlineKeyboardButton(name, callback_data=name)
        buttons.append(button)
    keyboard.add(*buttons)
    keyboard.add(buttonBack)
    bot.send_message(message.chat.id, f"Достопримечательности в {city}", reply_markup=keyboard)


def sendSubMenu(message):
    global stage
    stage = 1
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttonBeach = types.InlineKeyboardButton('Пляж', callback_data='beach')
    buttonCulture = types.InlineKeyboardButton('Достопримечательность', callback_data='culture')
    buttonBack = types.InlineKeyboardButton('Назад', callback_data='back')
    keyboard.add(buttonBeach, buttonCulture, buttonBack)
    bot.send_message(message.chat.id, 'Пляж / достопримечательность', reply_markup=keyboard)


# Запуск бота
bot.polling()
