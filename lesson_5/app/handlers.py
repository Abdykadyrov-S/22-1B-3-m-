from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram import Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


from app.keyboards import *

class Register(StatesGroup):
    full_name = State()
    age = State()
    email = State()


router = Router()

@router.message(CommandStart())
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.id}', reply_markup=inline_start_keyboard)
    register(message.from_user.id, message.from_user.full_name)
    global name
    name = ['qwert']

@router.callback_query(F.data == 'about')
async def about(callback: types.CallbackQuery):
    # await callback.answer("Вы выбрали О нас", show_alert=True)
    await callback.answer("Вы выбрали О нас")
    await callback.message.edit_text("О нас", reply_markup=inline_about)
    print(name) 

@router.callback_query(F.data == 'direction')
async def direction(callback: types.CallbackQuery):
    # await callback.answer("Вы выбрали О нас", show_alert=True)
    await callback.answer("Вы выбрали направления")
    await callback.message.edit_text("Наши действующие направления", reply_markup=await inline_direction())

@router.callback_query(F.data == 'profile')
async def get_profile(callback: types.CallbackQuery):
    user = get_user(callback.from_user.id)
    await callback.message.edit_text(f'{user}', reply_markup=inline_update)

@router.callback_query(F.data == 'update_profile')
async def update_profile(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("Обновите профиль")
    await callback.message.answer("Введите ФИО")
    await state.set_state(Register.full_name)

@router.message(Register.full_name)
async def update_profile_1(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await message.answer("Введите возраст")
    await state.set_state(Register.age)

@router.message(Register.age)
async def update_profile_2(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите email")
    await state.set_state(Register.email)

@router.message(Register.email)
async def update_profile_3(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Регистрация завершена")
    data = await state.get_data()
    full_name = data['full_name']
    age = data['age']
    email = data['email']
    await message.answer(f'Ваши данные: \nФИО: {full_name} \nВозраст: {age} \nemail: {email}')
    update_profile_in_db(message.from_user.id, full_name, age, email)
    await state.clear()

