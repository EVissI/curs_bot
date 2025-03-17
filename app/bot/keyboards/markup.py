from typing import Dict
from aiogram.types import ReplyKeyboardMarkup,ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

del_kbd = ReplyKeyboardRemove()


class MainKeyboard:
    __user_kb_texts_dict = {
        'currency': 'Курсы валют',
        'about_us': 'О нас',
    }


    @staticmethod
    def get_user_kb_texts() -> Dict[str, str]:
        """
        'currency'\n
        'about_us'
        """
        return MainKeyboard.__user_kb_texts_dict

    @staticmethod
    def build_main_kb() -> ReplyKeyboardMarkup:
        kb = ReplyKeyboardBuilder()

        for val in MainKeyboard.get_user_kb_texts().values():
            kb.button(text=val)
        kb.adjust(len(MainKeyboard.get_user_kb_texts()))

        return kb.as_markup(resize_keyboard=True)
    