from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


keyboard_buy = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(
        text='Купить подписку на канал ✅',
        callback_data='buy'
    )]]

)