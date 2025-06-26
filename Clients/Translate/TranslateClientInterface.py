from abc import ABC, abstractmethod

class TranslateClientInterface(ABC):
    @abstractmethod
    async def translate(self, source_lang: str, target_lang: str, text: str) -> str:
        pass