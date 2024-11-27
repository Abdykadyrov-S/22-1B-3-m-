from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram import Router
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

bot = Bot(token="8126121670:AAF2IiYJx_V77baXIO2-6NBF0N-lARcdxEI")

ADMIN_ID = [1904375259, '1904375259']

users = [1904375259, 1816628185, 6120470758, 7041997521, 7164957163, 1409305268, 7439688144]


from app.keyboards import *

class Register(StatesGroup):
    full_name = State()
    age = State()
    email = State()

class Mailing(StatesGroup):
    text = State()

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


@router.message(Command('help'))
async def command_help(message: types.Message):
    await bot.send_message(message.chat.id, """
Доступные команды:
/start - для запуска/перезапуска бота
/help - для вывода команд""")
    

@router.message(Command('mailing'))
async def command_mailing(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMIN_ID:
        for i in ADMIN_ID:
            await bot.send_message(i, 'Введите сообщение для рассылки')
            await state.set_state(Mailing.text)


@router.message(Mailing.text)
async def echo(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    text = data['text']
    for i in users:
        await bot.send_message(i, f'Рассылка: {text}')
    await message.answer("Рассылка окончена")
