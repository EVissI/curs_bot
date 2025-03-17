from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.db.models import Сurrency

class СurrencyData(CallbackData, prefix="currency"):
    currency_name:str = None

def take_currency_info_kb(currencies:list[Сurrency])-> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for currency in currencies:
        kb.button(text=currency.currency_name_for_bot,callback_data=СurrencyData(
            currency_name=currency.currency_name
            ).pack()
        )
    kb.adjust(2)
    return kb.as_markup()