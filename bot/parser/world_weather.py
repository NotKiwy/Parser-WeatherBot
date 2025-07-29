import asyncio
import aiohttp
from bs4 import BeautifulSoup
from typing import List

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 YaBrowser/25.6.0.0 Safari/537.36',
    'Accept-Language': 'ru,en;q=0.9'
}

async def _get_info_(cou: str, city: str) -> List[str] | int:
    url = f"https://world-weather.ru/pogoda/{cou}/{city}/"
    async with aiohttp.ClientSession() as sess:
        async with sess.get(url=url, headers=headers) as resp:
            html = await resp.text()
            soup = BeautifulSoup(html, "html.parser")
            try:
                weather = soup.find("div", id="weather-now-number").text
                time = soup.find("em", class_="tooltip").find_next_sibling("b").text
                etc = soup.find("div", id="weather-now-description")

                alllist = [dd.text for dd in etc.find_all("dd")]
                alllist.append(weather)
                alllist.append(time)

                return alllist
            except AttributeError:
                return 0
