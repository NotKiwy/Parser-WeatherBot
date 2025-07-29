from googletrans import Translator
import asyncio

async def _translate_(text: str, to='en'):
    tr = Translator()
    res = await tr.translate(text=text, src='ru', dest=to)
    return res.text.lower()