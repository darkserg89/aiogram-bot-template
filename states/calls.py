from aiogram.dispatcher.filters.state import StatesGroup,State


class Call(StatesGroup):
    #Класс состояний для хэндлера call
    number = State()