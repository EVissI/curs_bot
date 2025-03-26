from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from loguru import logger

from app.bot.common.messages import TEXT
from app.bot.keyboards.markup import MainKeyboard
from app.bot.routers.user_routers import user_router

from app.db.dao import UserDAO
from app.db.database import async_session_maker
from app.db.models import User
from app.db.schemas import UserModel, UserFilter

main_router = Router()
main_router.include_router(user_router)

@main_router.message(CommandStart())
async def cmd_command_start(message: Message):
    try:
        async with async_session_maker() as session:
            user = await UserDAO.find_one_or_none(session, filters=UserFilter(telegram_id=message.from_user.id))
            if user:
                await message.answer(
                    TEXT.get('start'),
                    reply_markup=MainKeyboard.build_main_kb()
                )
                return
            new_user = UserModel(
                telegram_id=message.from_user.id,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                username=message.from_user.username
            )
            await UserDAO.add(session, new_user)
            await message.answer(
                    TEXT.get('start'),
                    reply_markup=MainKeyboard.build_main_kb()
                )
    except Exception as e:
        pass