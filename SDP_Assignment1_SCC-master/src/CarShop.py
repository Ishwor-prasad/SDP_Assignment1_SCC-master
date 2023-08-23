from car_factory import CarFactory  # Assuming you have CarFactory class defined
from car_type import CarType

class CarShop:
    car = None

    @staticmethod
    def get_car_factory(car_type):
        return {
            CarType.RACING: RacingCarFactory,
            CarType.PRIVATE: PrivateCarFactory,
            CarType.SUV: SUVCarFactory,
            CarType.MILITARY: MilitaryCarFactory
        }.get(car_type)()

    @staticmethod
    def order_car(color, car_type, region, brand):
        pass  # Implement in derived shops


class FordUSA(CarShop):
    @staticmethod
    def order_car(color, car_type):
        car_factory = CarShop.get_car_factory(car_type)
        car = car_factory.create_car(color, "USA", "Ford")
        return car


class FordAsia(CarShop):
    @staticmethod
    def order_car(color, car_type):
        car_factory = CarShop.get_car_factory(car_type)
        car = car_factory.create_car(color, "Asia", "Ford")
        return car


class FerrariUSA(CarShop):
    @staticmethod
    def order_car(color, car_type):
        car_factory = CarShop.get_car_factory(car_type)
        car = car_factory.create_car(color, "USA", "Ferrari")
        return car


class FerrariAsia(CarShop):
    @staticmethod
    def order_car(color, car_type):
        car_factory = CarShop.get_car_factory(car_type)
        car = car_factory.create_car(color, "Asia", "Ferrari")
        return car


class BMWUSA(CarShop):
    @staticmethod
    def order_car(color, car_type):
        car_factory = CarShop.get_car_factory(car_type)
        car = car_factory.create_car(color, "USA", "BMW")
        return car


class BMWAsia(CarShop):
    @staticmethod
    def order_car(color, car_type):
        car_factory = CarShop.get_car_factory(car_type)
        car = car_factory.create_car(color, "Asia", "BMW")
        return car


class ToyotaUSA(CarShop):
    @staticmethod
    def order_car(color, car_type):
        car_factory = CarShop.get_car_factory(car_type)
        car = car_factory.create_car(color, "USA", "Toyota")
        return car


class ToyotaAsia(CarShop):
    @staticmethod
    def order_car(color, car_type):
        car_factory = CarShop.get_car_factory(car_type)
        car = car_factory.create_car(color, "Asia", "Toyota")
        return car
