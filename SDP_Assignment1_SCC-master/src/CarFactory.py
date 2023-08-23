from car import Car  # Assuming you have a Car class defined
from color import Color
from body_design import BodyDesign
from automated_ai import AutomatedAI

class CarFactory:
    car = None

    @staticmethod
    def create_car(color, region, brand):
        pass  # Implement in derived factories

    @staticmethod
    def get_color(color):
        pass  # Implement in derived factories

    @staticmethod
    def get_design_by_brand(design):
        pass  # Implement in derived factories

    @staticmethod
    def get_automated_ai(region):
        pass  # Implement in derived factories


class RacingCarFactory(CarFactory):
    @staticmethod
    def create_car(color, region, brand):
        car = RacingCar(
            CC1800(),
            SlickTire(),
            LadderFrameChassis(),
            HighPoweredAC(),
            CarFactory.get_color(color),
            CarFactory.get_design_by_brand(brand),
            CarFactory.get_automated_ai(region),
            RacingCarSeat()
        )
        return car


class PrivateCarFactory(CarFactory):
    @staticmethod
    def create_car(color, region, brand):
        car = PrivateCar(
            CC1300(),
            SpareTire(),
            BackboneChassis(),
            LowPoweredAC(),
            CarFactory.get_color(color),
            CarFactory.get_design_by_brand(brand),
            CarFactory.get_automated_ai(region),
            PrivateCarSeat()
        )
        return car


class SUVCarFactory(CarFactory):
    @staticmethod
    def create_car(color, region, brand):
        car = SUV(
            CC1700(),
            WhitewallTire(),
            LadderFrameChassis(),
            HighPoweredAC(),
            CarFactory.get_color(color),
            CarFactory.get_design_by_brand(brand),
            CarFactory.get_automated_ai(region),
            SUVCarSeat()
        )
        return car


class MilitaryCarFactory(CarFactory):
    @staticmethod
    def create_car(color, region, brand):
        car = MilitaryCar(
            CC2100(),
            SnowTire(),
            LadderFrameChassis(),
            HighPoweredAC(),
            CarFactory.get_color(color),
            CarFactory.get_design_by_brand(brand),
            CarFactory.get_automated_ai(region),
            MilitaryCarSeat()
        )
        return car
