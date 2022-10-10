from aiogram import Bot, Dispatcher, executor, types
from app import get_text
from io import BytesIO
import os
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token=os.getenv("TEXT_EXTRACTOR_API_KEY"))
dp = Dispatcher(bot)
lang = "rus+eng"

@dp.message_handler(commands="lang")
async def cmd_start(message: types.Message):
    kb = [
        [KeyboardButton(text="RU"),
        KeyboardButton(text="EN"),
        KeyboardButton(text="EN+RU")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("What language? Язык для распознавания текста?", reply_markup=keyboard)

@dp.message_handler(text="RU")
async def with_puree(message: types.Message):
    global lang
    lang = "rus"
    await message.reply("Choosed RU. Выбран русский язык.", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="EN")
async def with_puree(message: types.Message):
    global lang
    lang = "eng"
    await message.reply("Choosed EN. Выбран английский язык.", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="EN+RU")
async def with_puree(message: types.Message):
    global lang
    lang = "eng"
    await message.reply("Choosed EN + RU. Could be more artefacts. Выбраны английский и русский языки. Может быть больше артефактов.", reply_markup=ReplyKeyboardRemove())

@dp.message_handler()
async def kb_answer(message: types.Message):
    if (len(message.text) > 0):
        await message.answer('Send a photo of text. Type /lang to choose a language. \n\
Пришлите фото с текстом. Наберите /lang для смены распознаваемого языка \n\n')
    if (len(message.text) > 0):
        await message.answer('Make sure that your document has a white background, readable black letters and picture is not rotated. \n\
Пожалуйста, убедитесь что ваш документ имеет белый фон, буквы читаемы и черного цвета, а фото не перевернуто. \n\n')
    if lang == "rus+eng":
        await message.answer('Choosed EN+RU. If your document is in one language, please select it. Then you will have fewer artifacts. \n\
Выбран английский+русский. Если ваш документ на одном языке, пожалуйста выберите его. Тогда у вас будет меньше артефаков.')




@dp.message_handler(content_types=['photo'])
async def photo(message: types.Message):
    global lang
    await message.photo[-1].download()
    text = get_text(lang)
    #message.photo[-1].download()
    #text = get_text(bytes)
    await message.answer(text)

executor.start_polling(dp, skip_updates = True)