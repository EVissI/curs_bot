from typing import Optional
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from loguru import logger
from app.bot.common.messages import TEXT
from app.bot.keyboards.markup import MainKeyboard
from app.db.models import Сurrency
from app.db.dao import CurencyDAO
from app.db.database import async_session_maker
from app.db.schemas import СurrencyFilter
user_router = Router()

@user_router.message(F.text == MainKeyboard.get_user_kb_texts().get('about_us'))
async def cmd_about_us(message: Message):
    await message.answer(TEXT.get('about_us'))

@user_router.message(F.text == MainKeyboard.get_user_kb_texts().get('USDT'))
async def cmd_currency(message: Message):
    async with async_session_maker() as session:
        USDT: Optional[Сurrency] = await CurencyDAO.find_one_or_none(session,filters=СurrencyFilter(currency_name='USDT'))
    if not USDT:
        await message.answer(TEXT.get('no_currency'))
        return
    await message.answer(TEXT.get('currency_info').format(currency_name = USDT.currency_name, currency_value_buy = USDT.buy_value, currency_value_sell = USDT.sell_value))

@user_router.message(F.text == MainKeyboard.get_user_kb_texts().get('USD'))
async def cmd_currency(message: Message):
    async with async_session_maker() as session:
        USD: Optional[Сurrency] = await CurencyDAO.find_one_or_none(session,filters=СurrencyFilter(currency_name = 'USD'))
    if not USD:
        await message.answer(TEXT.get('no_currency'))
        return
    await message.answer(TEXT.get('currency_info').format(currency_name = USD.currency_name, currency_value_buy = USD.buy_value, currency_value_sell = USD.sell_value))