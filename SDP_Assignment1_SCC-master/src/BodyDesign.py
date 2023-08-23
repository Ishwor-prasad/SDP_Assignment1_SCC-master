from abc import ABC, abstractmethod

class BodyDesign(ABC):
    @abstractmethod
    def get_body_design_type(self):
        pass

    @abstractmethod
    def get_body_design_price(self):
        pass


class FordBodyDesign(BodyDesign):
    def get_body_design_type(self):
        return "Ford"

    def get_body_design_price(self):
        return 100000


class FerrariBodyDesign(BodyDesign):
    def get_body_design_type(self):
        return "Ferrari"

    def get_body_design_price(self):
        return 200000


class ToyotaBodyDesign(BodyDesign):
    def get_body_design_type(self):
        return "Toyota"

    def get_body_design_price(self):
        return 300000


class BMWBodyDesign(BodyDesign):
    def get_body_design_type(self):
        return "BMW"

    def get_body_design_price(self):
        return 400000
