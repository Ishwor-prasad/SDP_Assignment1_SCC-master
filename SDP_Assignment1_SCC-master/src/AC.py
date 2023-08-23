from abc import ABC, abstractmethod

class AC(ABC):
    @abstractmethod
    def get_ac_type(self):
        pass

    @abstractmethod
    def get_ac_price(self):
        pass


class HighPoweredAC(AC):
    def get_ac_type(self):
        return "HighPowered"

    def get_ac_price(self):
        return 100
