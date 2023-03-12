from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import logging


TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f"Салам {message.from_user.full_name}"
    )


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("Следующий вопрос", callback_data="button_1")
    markup.add(button_1)

    question = "В каком городе живёт Сайтама?"
    answers = [
        "город V",
        "город A",
        "город Z",
        "город D",
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="я думал ты знаешь ответ!",
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("Следующий вопрос", callback_data="button_2")
    markup.add(button_1)

    question = "Кому принадлежит эта цитата Если герои убегают и прячутся, то кто тогда будет сражаться?"
    answers = [
        "Генос",
        "Бэнг",
        "Торнадо",
        "Сайтама",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="я думал ты знаешь ответ!",
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_2")
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("Следующий вопрос", callback_data="button_3")
    markup.add(button_1)


    question = "Что постоянно забывает Сайтама?"
    answers = [
        "лица и имена",
        "оплачивать щита",
        "закрывать дверь",
        "дорогу домой",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="я думал ты знаешь ответ!",
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_3")
async def quiz_4(call: types.CallbackQuery):
    question = "Что не входит в тренировку Сайтамы?"
    answers = [
        "100 отжиманий",
        "100 приседаний",
        "100 подтягиваний",
        "100 пресса",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="я думал ты знаешь ответ!",
    )


@dp.message_handler(commands=['mem'])
async def send_mem(message:types.message):
    with open('images/photo_2023-03-09_10-36-11-600x338.jpg','rb')as images:
        await message.answer_photo(photo=images)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.strip().isdigit():
        a = int(message.text.strip())
        square = a ** 2
        await message.answer(square)
    else:
        await bot.send_message(chat_id=message.from_user.id, text=message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)