import os
from typing import Any

from aiogram.client.session import aiohttp
from dotenv import load_dotenv, find_dotenv

from Clients.Horoscope.ClientInterface import ClientInterface

#TEMP
load_dotenv(find_dotenv())

class Client(ClientInterface):
    def __init__(self):
        self.url = os.getenv("HOROSCOPE_API_URL")

    async def post(self, endpoint: str, params: dict) -> Any | None:
        api_url = self.url + endpoint
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(api_url, params=params) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data.get("data", {}).get("horoscope_data", "Нет данных 😢")
                    else:
                        return None
        except Exception as e:
            return None