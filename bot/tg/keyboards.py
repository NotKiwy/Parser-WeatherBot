from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
import os

load_dotenv()
_supp = os.getenv("SUPP")
_comm = os.getenv("COMM")

wkb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🚀 Выбрать город", callback_data="_city")
        ],
        [
            InlineKeyboardButton(text="🛠 Поддержка", url=_supp),
            InlineKeyboardButton(text="🤝 Комьюнити", url=_comm)
        ]
    ]
)
