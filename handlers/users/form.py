from aiogram import types
from loader import dp
from states import Pers_data
from aiogram.dispatcher import FSMContext


# Эхо хендлер, куда летят текстовые сообщения при испльзовавние команды /form
@dp.message_handler(commands=['form'])
async def enter_form(message: types.Message,state:FSMContext):
    #Спрашиваем первый вопрос
    await message.answer(f"Пожалуйста введите ФИО")
    #Изменяем состояние, что имя мы спросили
    await Pers_data.name.set()


@dp.message_handler(state=Pers_data.name)
async def enter_email(message: types.Message,state:FSMContext):
    #Записываем ответ на первый вопрос. !Обатить внимание, что ответ прилетает в следующий хэндлер
    answer = message.text
    #Записываем ответ на вопрос в опер. память
    await state.update_data(name=answer)
    await message.answer(f"Пожалуйста введите ваш email")
    #Отмечаем, что вопрос по email был задан тоже.
    await Pers_data.email.set()


@dp.message_handler(state=Pers_data.email)
async def enter_phone(message: types.Message,state:FSMContext):
    answer=message.text
    await state.update_data(email=answer)
    await message.answer(f"Пожалуйста введите ваш телефон")
    await Pers_data.phone.set()
@dp.message_handler(state=Pers_data.phone)
async def send_result(message: types.Message,state=FSMContext):
    answer = message.text
    await state.update_data(phone=answer)
    data = await state.get_data()
    #Вывести словарь полученных данных.
    #print((data))
    await message.answer(data)
    #Удалить данные из оперативной памяти
    await state.finish()