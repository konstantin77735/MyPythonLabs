from abc import ABC, abstractmethod

class Discountable(ABC):
    @abstractmethod
    def ask_discount(self):
        pass

    @abstractmethod
    def get_discount(self):
        pass

    @abstractmethod
    def set_discount(self, discount):
        pass

    @abstractmethod
    def remove_discount(self):
        pass

    @abstractmethod
    def get_discounted_price(self, discount):
        pass
