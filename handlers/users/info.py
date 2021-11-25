from aiogram import types
from loader import dp
from data.config import ADMINS


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(commands=['info'])
async def bot_echo(message: types.Message):
    await message.answer(f"Пожалуйста введите ФИО,"
                         f"Номер телефона\n"
                         f"Возраст")

@dp.message_handler(commands=['myuserid'])
async def bot_echo(message: types.Message):
    await message.answer(f"Your user id is: { message.from_user.id }")