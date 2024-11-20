from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram import Router


from app.keyboards import *

router = Router()

@router.message(CommandStart())
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.id}', reply_markup=inline_start_keyboard)

@router.callback_query(F.data == 'about')
async def about(callback: types.CallbackQuery):
    # await callback.answer("Вы выбрали О нас", show_alert=True)
    await callback.answer("Вы выбрали О нас")
    await callback.message.edit_text("О нас", reply_markup=inline_about)


@router.callback_query(F.data == 'direction')
async def direction(callback: types.CallbackQuery):
    # await callback.answer("Вы выбрали О нас", show_alert=True)
    await callback.answer("Вы выбрали направления")
    await callback.message.edit_text("Наши действующие направления", reply_markup=await inline_direction())

