#Хэндлер для звонков через телеграмм
from aiogram import types
from loader import dp
from states import Call
from aiogram.dispatcher import FSMContext

# Эхо хендлер, куда летят текстовые сообщения при испльзовавние команды /call
@dp.message_handler(commands=['call'])
async def enter_call(message: types.Message,state:FSMContext):
    #Спрашиваем номер телефона
    await message.answer(f"Please enter the number")
    #Изменяем состояние, что имя мы спросили
    await Call.number.set()

@dp.message_handler(state=Call.number)
async def enter_number(message: types.Message,state:FSMContext):
    #Сохраняем номер телефона
    answer = await message.answer()
    state.update_data(number=answer)
    #Здесь будет функция ориджинэйт для звонка через астер.
    await message.answer("Calling")

