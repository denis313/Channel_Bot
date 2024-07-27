import logging
from datetime import date

from bot import bot
from config import db_config
from database.requests import DatabaseManager
from keyboards import keyboard_buy
from lexicon import lexicon

logger = logging.getLogger(__name__)
dsn = db_config()
db_manager = DatabaseManager(dsn=dsn)


async def check_status():
    logging.debug(f'check_status')
    now = date.today()
    users = await db_manager.get_users()
    for user in users:
        date_user = user.subscription_end_date
        days = date_user - now
        if days.days == 2:
            await db_manager.update_user(user_id=user.user_id, user_data={'subscription_status': False})
            await bot.send_message(chat_id=user.user_id, text=lexicon['end_sub'], reply_markup=keyboard_buy)
        elif days.days <= 0:
            await db_manager.delete_user(user_id=user.user_id)
            await bot.send_message(chat_id=user.user_id, text=lexicon['del_user'], reply_markup=keyboard_buy)
            await bot.ban_chat_member(chat_id=-1002192877844, user_id=user.user_id)
            await bot.unban_chat_member(chat_id=-1002192877844, user_id=user.user_id)
            logging.debug(f'Kick user by id={user.user_id}')
