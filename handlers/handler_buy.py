import logging

from aiogram import F, Router, Bot
from aiogram.types import Message, CallbackQuery, LabeledPrice, PreCheckoutQuery
from config import admin_id
from lexicon import lexicon

# from LEXICON.lexicon import LEXICON_Creator, LEXICON_keyboard, LEXICON_FSM
# from config_data.config import DATABASE_URL
# from database.requests import DatabaseManager
# from filters.filter import IsPrivate, IsCreator
# from handlers.general.message_profile import profile
# from keyboards.callback_data_classes import SeatsFactory
# from keyboards.general_keyboards import keyboard_stock, keyboard_change_stock
# from services.services import random_assignment

logger = logging.getLogger(__name__)
router = Router()


@router.callback_query()
async def buy_subscribe(callback: CallbackQuery, bot: Bot):
    await bot.send_invoice(
        chat_id=callback.from_user.id,
        need_name=True,
        need_email=True,
        need_phone_number=True,
        title='Подписка на канал',
        description='Подписка на платный закрытый канал',
        provider_token="381764678:TEST:89489",
        currency='RUB',
        payload='buy_subscribe',
        start_parameter='text',
        prices=[
            LabeledPrice(label="rub", amount=300 * 100)
        ]
    )


@router.pre_checkout_query()
async def process_pre_check(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@router.message(F.successful_payment)
async def successful_payment_handler(message: Message, bot: Bot):
    successful_payment = message.successful_payment
    print(f'Successful payment: {successful_payment}')
    await bot.send_message(chat_id=int(admin_id()),
                           text=lexicon['new_user'].format(user_full_name=successful_payment.order_info.name,
                                                           user_id=message.from_user.id,
                                                           user_email=successful_payment.order_info.email,
                                                           user_phone=successful_payment.order_info.phone_number))
