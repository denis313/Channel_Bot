from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import Message

from database.requests import DatabaseManager
from lexicon import lexicon
from config import DATABASE_URL

router = Router()
router.message.filter(F.chat.type == 'private')
dsn = DATABASE_URL
db_manager = DatabaseManager(dsn=dsn)


@router.message(StateFilter(default_state))
async def start_command(message: Message):
    await db_manager.create_tables()
    await message.answer(lexicon['other'])
