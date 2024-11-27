import logging
import asyncio
import os

from aiogram import Bot, Dispatcher, types, F
from aiogram.types import BotCommand

from app.handlers import router, bot


# token = os.environ.get('token')
# print(token)

dp = Dispatcher()


command = [BotCommand(command='start', description='Начать')]

async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_routers(router)
    # print(name)
    await dp.start_polling(bot)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("выход")
