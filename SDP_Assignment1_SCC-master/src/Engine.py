from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def get_engine_type(self):
        pass

    @abstractmethod
    def get_engine_price(self):
        pass


class CC1300(Engine):
    def get_engine_type(self):
        return "CC1300"

    def get_engine_price(self):
        return 100000


class CC1700(Engine):
    def get_engine_type(self):
        return "CC1700"

    def get_engine_price(self):
        return 200000


class CC1800(Engine):
    def get_engine_type(self):
        return "CC1800"

    def get_engine_price(self):
        return 300000


class CC2100(Engine):
    def get_engine_type(self):
        return "CC2100"

    def get_engine_price(self):
        return 400000
