from abc import ABC, abstractmethod
from random import uniform

class Recyclable(ABC):
    @abstractmethod
    def get_recycled_price(self) -> float:
        pass

    @abstractmethod
    def get_new_price_info(self) -> str:
        pass

    @abstractmethod
    def utilize(self, utilized: bool):
        pass
