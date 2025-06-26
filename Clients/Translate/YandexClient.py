import os

from aiohttp import ClientSession
from dotenv import load_dotenv, find_dotenv

from Clients.Translate.TranslateClientInterface import TranslateClientInterface

load_dotenv(find_dotenv())

class YandexClient(TranslateClientInterface):
    def __init__(self):
        self.folderId = os.getenv("YANDEX_TRANSLATE_FOLDER_KEY")
        self.apiKey = os.getenv("YANDEX_TRANSLATE_API_KEY")
        self.url = "https://translate.api.cloud.yandex.net/translate/v2/translate"

    async def translate(self, source_lang: str, target_lang: str, text: str) -> str:
        endpoint = f"{self.url}"
        try:
            async with ClientSession() as session:
                async with session.post(endpoint, json={
                    "texts": [text],
                    "targetLanguageCode": "ru",
                    "folderId": self.folderId,
                }, headers={'Authorization': f"Api-Key {self.apiKey}"}) as response:
                    if response.status == 200:
                        data = await response.json()
                        return (
                            data.get("translations")[0].get("text")
                            if data.get("translations") and isinstance(data["translations"], list)
                            else "Нет перевода 😢"
                        )
                    else:
                        return f"Ошибка: {response.status}"
        except Exception as e:
            return f"Ошибка: {str(e)}"
