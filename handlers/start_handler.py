from aiogram import Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message

from keyboards import keyboard_buy
# from database.requests import DatabaseManager
# from functions import convert_to_string
# from keyboards.keyboards import admin_keyboard, person
from lexicon import lexicon
from config import DATABASE_URL

router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def start_command(message: Message):
    await message.answer(lexicon['start'], reply_markup=keyboard_buy)

