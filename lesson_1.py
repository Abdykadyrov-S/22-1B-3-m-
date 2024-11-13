from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import asyncio 

# Dispatcher - это то бологодоря чему бот отвечает
# F - мы его используем когда бот принимает text в место comand
# CommandStart - нужен для того чтобы давать  старт для нашего бота
# Command  - нужен для того чтобы давать команды по типу /start /help и тд
# asyncio - нужен для того чтобы твой бот был ассинхронным
# Message - нужет для того чтобы бот принимал текст от юзера

bot = Bot(token='7839930317:AAFnKEP-rraQdaEZ8M0LZMS21qW4D8YYxWE') # Нужно вставить то что скопировали 
dp = Dispatcher() #Для того чтобы передать запроc

@dp.message(CommandStart()) # Для старта 
async def start(message: Message):
    await message.answer("Привет!") # А ансвер просто выводит ответ не отвечая нее
    
@dp.message(Command('help'))  # Можно заменить на русский язык слово хелп, можно вообще заменить на все что угодно 
async def help(message: Message):
    await message.reply("Чем могу помочь?") # Реплай отвечает на сообщение 
    
@dp.message(Command('about'))
async def about(message: Message):
    await message.reply('Geeks - это айти курсы в Оше')
    
@dp.message(Command('contact'))
async def contact(message: Message):
    await message.reply_contact(phone_number='+996508070508', last_name='Aslan', first_name='Baibalaev')
    
@dp.message(Command('location'))
async def location(message: Message):
    await message.reply_location(latitude=40.51931846586533, longitude=72.80297788183063)
    
@dp.message(F.text.lower() == 'исхак')
async def iskhak(message: Message):
    await message.reply('Ученик 3 - месяца')
    
@dp.message(F.text.lower() == 'фото')
async def photo(message: Message):
    await message.reply_photo(photo='https://wallpapercat.com/w/full/f/2/a/210801-3840x2160-desktop-4k-lebron-james-background-image.jpg')
    
@dp.message(F.text.lower() == 'стикер')
async def sticker(message: Message):
    await message.reply_sticker(sticker='')

async def main():
    await dp.start_polling(bot)
                                   # Нужно завопнить вот эти 4 блока
asyncio.run(main())
