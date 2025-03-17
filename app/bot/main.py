from app.bot.routers.main_router import main_router
from app.config import setup_logger

logger = setup_logger("bot")

import asyncio
from aiogram.types import BotCommand, BotCommandScopeDefault
from loguru import logger

from app.config import bot, dp

async def set_commands():
    commands = [
        BotCommand(command="start", description="Начать работу"),
    ]
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())

async def start_bot():
    await set_commands()
    logger.info("Бот успешно запущен.")

async def stop_bot():
    logger.error("Бот остановлен!")

async def main():
    # регистрация роутеров
    dp.include_router(main_router)
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    try:       
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
