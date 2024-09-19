import requests
import random
import telebot
from bs4 import BeautifulSoup as bs
from telebot import types
import datetime

"""ENGLISH WORDS"""
dictionary = {}
list_with_english_words = []
list_with__russian_words = []
meaning_list = []
src = "https://tefl-tesol-certificate.com/blog/slova-dlya-urovnya-anglijskogo-c1-advanced-prodvinutyj"
req = requests.get(src)
soup = bs(req.text, 'lxml')
words = soup.find("div", class_='overflow', attrs='tr')

full_list = [' To abate [əˈbeɪt] Сокращать, уменшать, ослаблять',
             ' To abjure [əbˈʤʊə] Отказаться, отрекаться, воздерживаться',
             ' To dangle [ˈdæŋgl] Болтаться, зависать, висеть', ' To abscond [əbˈskɒnd] Скрыться, пропасть, уйти',
             ' To assuage [əˈsweɪʤ] Успокаивать, утешать, усмирять',
             ' To disabuse [ˌdɪsəˈbjuːz] Разочаровать, расстроить, развенчать',
             ' To equivocate [ɪˈkwɪvəkeɪt] Увиливать, оправдываться, оспаривать', ' To incise [ɪnˈsaɪz] Надрезать',
             ' To diminish [dɪˈmɪnɪʃ] Уменьшать', ' To jeopardize [ˈʤɛpədaɪz] Ставить под угрозу',
             ' To breed [briːd] Размножаться', ' To prevaricate [prɪˈværɪkeɪt] Преувеличивать',
             ' To recant [rɪˈkænt] Отказаться от показаний', ' To refute [rɪˈfjuːt] Опровергать',
             ' To ignoble [ɪgˈnəʊbl] Обольстить', ' To banish [ˈbænɪʃ Изгнать', ' To disavow [ˌdɪsəˈvaʊ] Отречься',
             ' To explode [ɪksˈpləʊd] Взорваться', ' To unearth [ ʌnˈɜːθ] Раскопать', ' To depict [dɪˈpɪkt] Отобразить',
             ' To unpick [ʌnˈpɪk] Распарывать, распустить', ' To originate [əˈrɪʤɪneɪt] Зарождаться',
             ' To pluck [plʌk] Вырывать', ' To amass [əˈmæs] Накапливать', ' To staff [stɑːf] Укомплектовать',
             ' To shrink [ʃrɪŋk] Сокращаться', ' To mold [məʊld] Лепить', ' To contrive [kənˈtraɪv] Придумывать',
             ' To entice [ɪnˈtaɪs] Завлекать', ' To pervade [pɜːˈveɪd] Пронизывать',
             ' To prevail [prɪˈveɪl] Преобладать', ' To supersede [ˌsjuːpəˈsiːd] Вытеснять',
             ' To redeem [rɪˈdiːm] Выкупить', ' To wrack [ræk] Потревожить', ' To mesh [mɛʃ] Зацеплять',
             ' To render [ˈrɛndə] Оказывать', ' To lease [liːs] Сдать в аренду',
             ' To stipulate [ˈstɪpjʊleɪt] Оговаривать', ' To decree [dɪˈkriː] Постановить',
             ' To reminisce [ˌrɛmɪˈnɪs] Вспоминать', ' To rarefy [ˈreərɪfaɪ] Редеть',
             ' To venerate [ˈvɛnəreɪt] Почитать', ' To hatch [hæʧ] Вылупляться', ' To anchor [ˈæŋkə] Бросить якорь',
             ' To inherit [ɪnˈhɛrɪt] Получить в наследство', ' To stab [stæb] Закалывать, нападать, вонзать',
             ' To sublet [ˌsʌbˈlɛt] Сдавать в субаренду', ' To outline [ˈaʊtlaɪn] Начертить, обрисовать, наметить',
             ' To infiltrate [ˈɪnfɪltreɪt] Проникнуь, внедриться, просачиваться',
             ' To utter [ˈʌtə] Произносить, изрекать, проговаривать',
             ' To vituperate [vɪˈtjuːpəreɪt] Издеваться, обижать',
             ' To waver [ˈweɪvə] Колебаться, извиваться, дрогнуть',
             ' To withstand [wɪðˈstænd] Выдерживать, устоять, терпеть', ' To swap [swɒp] Поменять местами, сменить',
             ' To coax [kəʊks] Соединить', ' To conspire [kənˈspaɪə] Сговориться', ' To append [əˈpɛnd] Приложить',
             ' To entail [ɪnˈteɪl] Влечь за собой', ' To repine [rɪˈpaɪn] Порицать',
             ' To glance [glɑːns] Бросить взгляд, мельком глянуть', ' To resort [rɪˈzɔːt] Прибегать',
             ' To substitute [ˈsʌbstɪtjuːt] Заменить', ' To surpass [sɜːˈpɑːs] Превзойти', ' To deem [diːm] Считать',
             ' To prophesy [ˈprɒfɪsaɪ] Пророчествовать', ' To unveil [ʌnˈveɪl] Раскрыть',
             ' To discard [ˈdɪskɑːd] Отказаться, списывать, отвергнуть', ' To eradicate [ɪˈrædɪkeɪt] Искоренить',
             ' To propagate [ˈprɒpəgeɪt] Распространять', ' To terminate [ˈtɜːmɪneɪt] Прекратить',
             ' To engross [ɪnˈgrəʊs] Захватить', ' To overtake [ˌəʊvəˈteɪk] Обгонять, нагнать, преодолеть',
             ' To shield [ ʃiːld] Укрыть, заслонить, оградить', ' To ingest [ɪnˈʤɛst] Проглотить',
             ' To malign [məˈlaɪn] Очернить', ' To exhibit [ɪgˈzɪbɪt] Выставлять',
             ' To extirpate [ˈɛkstɜːpeɪt] Уничтожить', ' To initiate [ɪˈnɪʃɪɪt] Инициировать',
             ' To adjoy [ ædʤɔɪ] Придерживаться', ' To delve [dɛlv] Углубиться',
             ' to vow [ vaʊ] Клясться, ручаться, обещать', ' to alienate [ˈeɪliəneɪt] отчуждать',
             ' to reimburse [ˌriːɪmˈbɜːs] возмещать', ' to disperse [dɪsˈpɜːs] Рассеивать, расходиться',
             ' to overlook [ˌəʊvəˈlʊk] упускать из виду',
             ' to dismantle [dɪsˈmæntl] Демонтировать, разобрать, убрать, разрушить',
             ' to exhilarate [ɪgˈzɪləreɪt] взбодриться', ' to thrill [θrɪl] возбуждать',
             ' to underpin [ˌʌndəˈpɪn] поддерживать', ' to follow-up [ˈfɒləʊˈʌp] следить',
             ' to predispose [ˌpriːdɪsˈpəʊz] Предрасполагать, склонять, располагать',
             ' to peer [pɪə] Равняться, сравнивать, подглядывать', ' to intervene [ˌɪntə(ː)ˈviːn] вмешиваться',
             ' to resonate [ˈrɛzəˌneɪt] резонировать',
             ' to contradict [ˌkɒntrəˈdɪkt] Противоречить, возражать, опровергнуть',
             ' to distil [dɪsˈtɪl] Дистиллировать, смягчать, рассеивать',
             ' to mitigate [ˈmɪtɪgeɪt] Смягчать, сгладить, ослабить',
             ' to bounce back [baʊns bæk] Отскочить, вернуться, возвращаться, восстановиться',
             ' To indulge [ɪnˈdʌlʤ] Побаловать, потакать, потворствовать',
             ' To sniff [snɪf] Нюхать, принюхиваться, сопеть']
for item in full_list:
    list_with_english_words.append(' '.join(item.split()[0:2]))
    list_with__russian_words.append(' '.join(item.split()[3:]))
for index in range(len(list_with_english_words)):
    dictionary[list_with_english_words[index]] = list_with__russian_words[index]

test_list = []
"""Parser Compliment"""
URL = 'https://love.romanticcollection.ru/blog/500-trogatelnyh-komplimentov-devushke/'
req = requests.get(URL)
req.encoding = 'UTF8'
soup = bs(req.text, 'lxml')
compliments = soup.find('div', class_="entry-content", attrs={'ol'}).find_all('li')
list_with_compliments = []
for i in compliments:
    list_with_compliments.append(str(i.text))
list_with_compliments = list_with_compliments[1:-1]

"""My Telegram Bot"""
bot = telebot.TeleBot('5977193219:AAFqzzucWd_-unRIqE7RmrBGCHwOnidW5JY')


@bot.message_handler(commands=['start'])
def start_command(message):
    """send image(monkey)"""
    image = open("monkeywithorange.jpg", 'rb')
    bot.send_photo(message.chat.id, image)


@bot.message_handler(commands=['course'])
def course(message):
    """function that still needs"""
    pass


@bot.message_handler(commands=['compliment'])
def compliment_sender(message):
    """Function that sends compliment"""
    random.shuffle(list_with_compliments)
    bot.send_message(message.chat.id, list_with_compliments[0])
    list_with_compliments.remove(list_with_compliments[0])
    if len(list_with_compliments) == 0:
        bot.send_message(message.chat.id, 'осымен бытты барнзге рахмет юху')

@bot.message_handler(commands=['time'])
def time_sender(message):
    bot.send_message(message.chat.id, f'Сейчас время {str(datetime.datetime.now())[10:16]}')


@bot.message_handler(commands=['my_instagram'])
def my_instagram(message):
    """Function that sends my instagram account"""
    markup1 = types.InlineKeyboardMarkup()
    markup1.add(types.InlineKeyboardButton('me', url='https://www.instagram.com/jaygana.arss/'))
    bot.send_message(message.chat.id, 'me', reply_markup=markup1)


@bot.message_handler(commands=['game'])
def game(message):
    """Started but did not finish"""
    s = [1, 2, 3, 4, 5, 6]
    bot.send_message(message.chat.id, random.choice(s))


@bot.message_handler(commands=['weather'])
def send_weather(message):
    input_message = bot.send_message(message.chat.id, 'Напишите название города:')
    bot.register_next_step_handler(input_message, get_weather)


def get_weather(message):
    message_from_user = message.text
    weather_token = "5522d207dfc0c9de1d47603860270cfe"
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message_from_user}&units=metric&appid={weather_token}')
        data = r.json()
        temperature = f"Температура в городе '{message_from_user.capitalize()}':\n{data['main']['temp']}°C"
        feels_like = f"Ощущается как {data['main']['feels_like']}°C"
        wind_speed = f"Скорость ветра {data['wind']['speed']}м/c"
        bot.send_message(message.chat.id, f'{temperature}\n{feels_like}\n{wind_speed}')
    except Exception as ex:
        bot.send_message(message.chat.id, 'Введите название города правильно!')


@bot.message_handler(commands=['words'])
def english_words(message):
    dictionary_keys = list(dictionary)[random.choice([i for i in range(100)])]
    bot.send_message(message.chat.id, f"{dictionary_keys}: {dictionary[dictionary_keys]}")


@bot.message_handler(commands=['test_vocabulary'])
def test_vocabulary(message):
    """1) Send one english word
    2) There will be four buttons one have correct answer others not
    3) User should choose right answer and press one button
    4) If answer is correct good job
    5) Else send right answer"""
    global dictionary_keys
    dictionary_keys = list(dictionary)[random.choice([i for i in range(1, 101)])]

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    button_with_right_answer = types.KeyboardButton(text=dictionary[dictionary_keys])
    button_with_incorrect_answer = types.KeyboardButton(
        text=list(dictionary.values())[random.choice([i for i in range(100)])])
    button_with_incorrect_answer_two = types.KeyboardButton(
        text=list(dictionary.values())[random.choice([i for i in range(100)])])
    button_with_incorrect_answer_three = types.KeyboardButton(
        text=list(dictionary.values())[random.choice([i for i in range(100)])])
    list_button = [button_with_incorrect_answer, button_with_right_answer, button_with_incorrect_answer_two,
                   button_with_incorrect_answer_three]
    random.shuffle(list_button)
    keyboard.add(list_button[0], list_button[1], list_button[2], list_button[3])
    send = bot.send_message(message.chat.id, dictionary_keys, reply_markup=keyboard)
    bot.register_next_step_handler(send, check_answer)


def check_answer(message):
    count = 0
    test_list.append(message.text)
    if message.text in dictionary[dictionary_keys]:
        count += 1
        bot.send_message(message.chat.id, f'good job')
    else:
        bot.send_message(message.chat.id, f"nice try")
        bot.send_message(message.chat.id, f"Correct answer: {dictionary[dictionary_keys]}")



@bot.message_handler(content_types=['text'])
def sending(message):
    string = message.text
    bot.send_message(message.chat.id, f'өөөөөөөөөөөөөөөөөөөөө')


bot.polling(none_stop=True)
