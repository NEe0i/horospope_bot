from abc import ABC, abstractmethod

class HoroscopeInterface(ABC):
    @abstractmethod
    def get_horoscope(self, zodiac: str) -> dict:
        pass