from abc import ABC, abstractmethod

class Chassis(ABC):
    @abstractmethod
    def get_chassis_type(self):
        pass

    @abstractmethod
    def get_chassis_price(self):
        pass


class TabularChassis(Chassis):
    def get_chassis_type(self):
        return "Tabular"

    def get_chassis_price(self):
        return 100000


class BackboneChassis(Chassis):
    def get_chassis_type(self):
        return "Backbone"

    def get_chassis_price(self):
        return 200000


class LadderFrameChassis(Chassis):
    def get_chassis_type(self):
        return "LadderFrame"

    def get_chassis_price(self):
        return 300000
