from aiohttp import ClientSession
from dotenv import load_dotenv, find_dotenv

from Clients.Translate.TranslateClientInterface import TranslateClientInterface

load_dotenv(find_dotenv())

class LingvaClient(TranslateClientInterface):
    def __init__(self):
        self.url = "https://lingva.ml/api/v1"

    async def translate(self, source_lang: str, target_lang: str, text: str) -> str:
        endpoint = f"{self.url}/{source_lang}/{target_lang}/{text}"
        try:
            async with ClientSession() as session:
                async with session.get(endpoint) as response:
                    if response.status == 200:
                        data = await response.json()
                        return data.get("translation", "Нет перевода 😢")
                    else:
                        return f"Ошибка: {response.status}"
        except Exception as e:
            return f"Ошибка: {str(e)}"
