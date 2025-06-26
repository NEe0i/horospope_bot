import logging
import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from dotenv import load_dotenv, find_dotenv

from Clients.Horoscope.Client import Client
from Services.Horoscope.HoroscopeService import HoroscopeService

load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

logging.basicConfig(level=logging.INFO)

#Service and Client - DI
HoroscopeClient = Client()
HoroscopeService = HoroscopeService(HoroscopeClient)

zodiacs = [
    "♈ Овен", "♉ Телец", "♊ Близнецы", "♋ Рак",
    "♌ Лев", "♍ Дева", "♎ Весы", "♏ Скорпион",
    "♐ Стрелец", "♑ Козерог", "♒ Водолей", "♓ Рыбы"
]

# Общий список гороскопов (если API не сработает)
common_horoscopes = [
    "Сегодня вас ждёт удача!",
    "Будьте осторожны в финансовых вопросах.",
    "Возможны неожиданные приятные встречи.",
    "Лучший день для новых начинаний!",
    "Слушайте свою интуицию – она вас не подведёт."
]

keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text=zodiac)] for zodiac in zodiacs],
    resize_keyboard=True
)

async def get_horoscope_from_api(sign: str) -> str:
    return await HoroscopeService.get_horoscope(sign)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Выбери свой знак зодиака, чтобы получить гороскоп:", reply_markup=keyboard)

@dp.message()
async def zodiac_selected(message: types.Message):
    sign = message.text.strip()
    if sign in zodiacs:
        horoscope = await get_horoscope_from_api(sign)
        if horoscope:
            await message.answer(f"🔮 Гороскоп для {sign}:\n\n{horoscope}")
        else:
            prediction = random.choice(common_horoscopes)
            await message.answer(f"🔮 Гороскоп для {sign}:\n\n{prediction}")
    else:
        await message.answer("Пожалуйста, выбери знак зодиака из списка.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())