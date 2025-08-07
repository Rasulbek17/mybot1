import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
import logging
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(F.text)
async def echo_handler(message: Message):
    await message.answer(f"Сәлем! Сіз: {message.text} деп жаздыңыз.")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
