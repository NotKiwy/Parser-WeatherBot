from parser.world_weather import _get_info_
from api.libre_translate import _translate_
import tg.texts as text
import tg.keyboards as kb

from aiogram import F, types, Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import Command
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

import dotenv
import asyncio
import os

dotenv.load_dotenv()
token = os.getenv("TOKEN")

class Input(StatesGroup):
    waiter = State()

bot = Bot(
    token=token,
    default=DefaultBotProperties(parse_mode="HTML")
)
dp = Dispatcher()

@dp.message(Command('start'))
async def _cmd_start(m: types.Message):
    await m.reply(text.welcome.format(
        FN=m.from_user.first_name
    ), reply_markup=kb.wkb)

@dp.callback_query(F.data == "_city")
async def _call__city_(call: CallbackQuery, state: FSMContext):
    await call.message.reply(text.fsm)
    await state.set_state(Input.waiter)

@dp.message(Input.waiter)
async def _fsm_finish_(m: types.Message):
    state = m.text
    fin = []

    oldfin = state.split(', ')
    fin.append(await _translate_(oldfin[0]))
    fin.append(await _translate_(oldfin[1]))

    if len(fin) == 2:
        _getter_ = await _get_info_(fin[0], fin[1])
        if _getter_ != 0:
            await m.reply(text.answ.format(
                COU=(fin[0]).upper(),
                CITY=(fin[1]).upper(),
                TEMP=_getter_[8],
                TIME=_getter_[9],
                OTEMP=_getter_[0],
                DV=_getter_[1],
                VL=_getter_[2],
                VETER=_getter_[3],
                SVETER=_getter_[4],
                SKY=_getter_[5],
                SEEP=_getter_[6],
                IND=_getter_[7]
            ))
        else:
            await m.reply(text.err)
    else:
        await m.reply(text.err0)

async def setup():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(setup())
    except  KeyboardInterrupt:
        print("Stopped.")