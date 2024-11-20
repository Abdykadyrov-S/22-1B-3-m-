from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from app.db import *

inline_start_button = [
    [InlineKeyboardButton(text='Платформа', url='https://online.geeks.kg/'), InlineKeyboardButton(text='О нас', callback_data='about')]
]

inline_start_keyboard = InlineKeyboardMarkup(inline_keyboard=inline_start_button)

inline_about = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Контакты', url='https://online.geeks.kg/'), InlineKeyboardButton(text='Направления', callback_data='direction')]
])

# directions = ['Backend', 'Frontend', 'Ux_Ui']


async def inline_direction():
    directions = get_direction()
    keyboard = InlineKeyboardBuilder()
    for direction in directions:
        keyboard.add(InlineKeyboardButton(text=direction, callback_data=f'dir_{direction}'))
    return keyboard.adjust(2).as_markup()


