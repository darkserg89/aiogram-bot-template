from aiogram.dispatcher.filters.state import StatesGroup,State


class Pers_data(StatesGroup):
    #Класс состояний для хэндлера form
    name = State()
    email = State()
    phone = State()