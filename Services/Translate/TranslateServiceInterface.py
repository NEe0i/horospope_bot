from abc import ABC, abstractmethod

class TranslateServiceInterface(ABC):
    @abstractmethod
    def translate(self, source_lang: str, target_lang: str, text: str) -> str:
        pass