from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = [
    [KeyboardButton(text='меню'), KeyboardButton(text='контакты')],
    [KeyboardButton(text='о нас')]
]

keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберите кнопку')


menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Первое'), KeyboardButton(text='Второе'), KeyboardButton(text='Третье')],
    [KeyboardButton(text='Фасфуд'), KeyboardButton(text='Напитки'), KeyboardButton(text='Салаты')],
], one_time_keyboard=True)