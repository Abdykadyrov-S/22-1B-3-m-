import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import token

bot = Bot(token=token)
dp = Dispatcher()

buttons = [
    [KeyboardButton(text='меню'), KeyboardButton(text='контакты')],
    [KeyboardButton(text='о нас')]
]

keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберите кнопку')


menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Первое'), KeyboardButton(text='Второе'), KeyboardButton(text='Третье')],
    [KeyboardButton(text='Фасфуд'), KeyboardButton(text='Напитки'), KeyboardButton(text='Салаты')],
], one_time_keyboard=True)


@dp.message(CommandStart())
async def command_start(message: types.Message):
    await message.answer('Привет', reply_markup=keyboard)


@dp.message(Command('help'))
async def command_help(message: types.Message):
    await message.reply('Чем могу помочь?')


@dp.message(F.text == 'меню')
async def command_help(message: types.Message):
    await message.answer_photo('https://img.pikbest.com/templates/20210617/bg/021a63ef9eca1457db82d6a408986fab_38895.png', reply_markup=menu_keyboard)

   
@dp.message(F.text == 'контакты')
async def contact(message: types.Message):
    await message.reply_contact(phone_number='+996508070508', last_name='Aslan', first_name='Baibalaev')


@dp.message(F.text.in_({'привет', 'првет'}))
async def command_help(message: types.Message):
    await message.reply("Привет")

@dp.message()
async def echo(message: types.Message):
    await message.answer("я вас не понял")

async def main():
    await dp.start_polling(bot)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("выход")
