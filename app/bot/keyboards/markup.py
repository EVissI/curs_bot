from typing import Dict
from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

del_kbd = ReplyKeyboardRemove()


class MainKeyboard:
    __user_kb_texts_dict = {
        'USDT': 'Курс USDT',
        'USD': 'Курс доллара',
        'about_us': 'О нас',
    }


    @staticmethod
    def get_user_kb_texts() -> Dict[str, str]:
        """
        'USDT'\n
        'USD'\n
        'about_us'
        """
        return MainKeyboard.__user_kb_texts_dict

    @staticmethod
    def build_main_kb() -> ReplyKeyboardMarkup:
        kb = ReplyKeyboardBuilder()

        for val in MainKeyboard.get_user_kb_texts().values():
            kb.button(text=val)
        kb.adjust(2,1)

        return kb.as_markup(resize_keyboard=True)
    