import logging
import asyncio
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import BotCommand


token = os.environ.get('token')
print(token)

bot = Bot(token="8126121670:AAF2IiYJx_V77baXIO2-6NBF0N-lARcdxEI")
dp = Dispatcher()


command = [BotCommand(command='start', description='Начать')]

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("выход")
