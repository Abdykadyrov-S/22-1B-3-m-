from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram import Router

from app.keyrboards import *

router = Router()

@router.message(CommandStart())
async def command_start(message: types.Message):
    await message.answer('Привет', reply_markup=keyboard)


@router.message(Command('help'))
async def command_help(message: types.Message):
    await message.reply('Чем могу помочь?')


@router.message(F.text == 'меню')
async def command_help(message: types.Message):
    await message.answer_photo('https://img.pikbest.com/templates/20210617/bg/021a63ef9eca1457db82d6a408986fab_38895.png', reply_markup=menu_keyboard)

   
@router.message(F.text == 'контакты')
async def contact(message: types.Message):
    await message.reply_contact(phone_number='+996508070508', last_name='Aslan', first_name='Baibalaev')


@router.message(F.text.in_({'привет', 'првет'}))
async def command_help(message: types.Message):
    await message.reply("Привет")

@router.message()
async def echo(message: types.Message):
    await message.answer("я вас не понял")