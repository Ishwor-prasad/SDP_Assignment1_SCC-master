from abc import ABC, abstractmethod

class Color(ABC):
    @abstractmethod
    def get_color_type(self):
        pass

    @abstractmethod
    def get_color_price(self):
        pass


class RedColor(Color):
    def get_color_type(self):
        return "Red"

    def get_color_price(self):
        return 100000


class WhiteColor(Color):
    def get_color_type(self):
        return "White"

    def get_color_price(self):
        return 200000


class GreyColor(Color):
    def get_color_type(self):
        return "Grey"

    def get_color_price(self):
        return 300000


class BlackColor(Color):
    def get_color_type(self):
        return "Black"

    def get_color_price(self):
        return 400000
