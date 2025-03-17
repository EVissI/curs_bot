from typing import Optional
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from loguru import logger
from app.bot.common.messages import TEXT
from app.bot.keyboards.inline import take_currency_info_kb, СurrencyData
from app.bot.keyboards.markup import MainKeyboard
from app.db.models import Сurrency
from app.db.dao import CurencyDAO
from app.db.database import async_session_maker
from app.db.schemas import СurrencyFilter
user_router = Router()

@user_router.message(F.text == MainKeyboard.get_user_kb_texts().get('about_us'))
async def cmd_about_us(message: Message):
    await message.answer(TEXT.get('about_us'))

@user_router.message(F.text == MainKeyboard.get_user_kb_texts().get('currency'))
async def cmd_currency(message: Message):
    async with async_session_maker() as session:
        currencies: Optional[list[Сurrency]] = await CurencyDAO.find_all(session,filters=СurrencyFilter())
    if not currencies:
        await message.answer(TEXT.get('no_currency'))
        return
    await message.answer(TEXT.get('currency'),reply_markup=take_currency_info_kb(currencies))

@user_router.callback_query(СurrencyData().filter())
async def cmd_currency_info(query: CallbackQuery, callback_data: СurrencyData):
    await query.message.delete()
    async with async_session_maker() as session:
        currency: Optional[Сurrency] = await CurencyDAO.find_one_or_none(session,filters=СurrencyFilter(currency_name=callback_data.currency_name))
    await query.message.answer(TEXT.get('currency_info').format(currency_name = currency.currency_name, currency_value = currency.value))