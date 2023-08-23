from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self):
        self.engine = None
        self.tire = None
        self.chassis = None
        self.ac = None
        self.color = None
        self.body_design = None
        self.automated_ai = None
        self.seat = None

    @abstractmethod
    def get_car_price(self):
        pass

    @abstractmethod
    def get_car_details(self):
        pass
