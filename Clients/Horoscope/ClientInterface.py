from abc import ABC, abstractmethod

class ClientInterface(ABC):
    @abstractmethod
    async def post(self, endpoint: str, params: dict) -> str:
        pass