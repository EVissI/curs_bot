from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from loguru import logger

from app.bot.common.messages import TEXT
from app.bot.keyboards.markup import MainKeyboard
from app.bot.routers.user_routers import user_router

main_router = Router()
main_router.include_router(user_router)

@main_router.message(CommandStart())
async def cmd_command_start(message: Message):
    await message.answer(
        TEXT.get('start'),
        reply_markup=MainKeyboard.build_main_kb()
    )