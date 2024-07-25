# bot.py

import logging
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
import environ

# Import BASE_DIR from settings
from bot_api_project.settings import BASE_DIR
# Initialize environ
env = environ.Env()
# Read .env file
environ.Env.read_env(BASE_DIR / '.env')

API_URL_TIME = 'http://127.0.0.1:8000/api/current-datetime/'
API_URL_ADVISES = 'http://127.0.0.1:8000/api/random-advises/'
TOKEN = env('TELEGRAM_BOT_TOKEN')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    Send a welcome message with buttons.
    """
    keyboard = types.InlineKeyboardMarkup()
    time_button = types.InlineKeyboardButton("Котра година", callback_data='time')
    advise_button = types.InlineKeyboardButton("Надати поради", callback_data='advise')
    keyboard.add(time_button, advise_button)
    await message.reply("Натисніть кнопку:", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'time')
async def process_time_callback(callback_query: types.CallbackQuery):
    """
    Process time request and send current time.
    """
    try:
        response = requests.get(API_URL_TIME)
        response.raise_for_status()
        current_datetime = response.json().get('current_datetime')
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, f"Поточний час: {current_datetime}")
    except requests.exceptions.RequestException as e:
        await bot.send_message(callback_query.from_user.id, f"Помилка отримання часу: {e}")

@dp.callback_query_handler(lambda c: c.data == 'advise')
async def process_advise_callback(callback_query: types.CallbackQuery):
    """
    Process advise request and send random advises.
    """
    try:
        response = requests.get(API_URL_ADVISES)
        response.raise_for_status()
        advises = response.json()
        advises_text = "\n".join([advise['text'] for advise in advises])
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id, f"Поради:\n{advises_text}")
    except requests.exceptions.RequestException as e:
        await bot.send_message(callback_query.from_user.id, f"Помилка отримання порад: {e}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
