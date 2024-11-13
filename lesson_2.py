import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

from config import token

bot = Bot(token=token)
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start(message: types.Message):
    await message.answer('Привет')

@dp.message(Command('help'))
# if message == '/help':
#     command_help()
# else:
#     pass
async def command_help(message: types.Message):
    await message.answer('Чем могу помочь?')

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("выход")
