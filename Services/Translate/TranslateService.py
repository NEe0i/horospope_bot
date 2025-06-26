from Clients.Translate.TranslateClientInterface import TranslateClientInterface
from Services.Translate.TranslateServiceInterface import TranslateServiceInterface


class TranslateService(TranslateServiceInterface):

    def __init__(self, client: TranslateClientInterface):
        self.client = client

    async def translate(self, source_lang: str, target_lang: str, text: str) -> str:
        response = await self.client.translate(source_lang, target_lang, text)
        print(response)
        return response
