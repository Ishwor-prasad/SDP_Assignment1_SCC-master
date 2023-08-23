class ThickRainShieldDecorator(CarDecorator):
    def __init__(self, car):
        self.car = car

    def get_car_price(self):
        return self.car.get_car_price() + 1000

    def get_car_details(self):
        return self.car.get_car_details() + "\nThick Rain Shield"


class ThinRainShieldDecorator(CarDecorator):
    def __init__(self, car):
        self.car = car

    def get_car_price(self):
        return self.car.get_car_price() + 500

    def get_car_details(self):
        return self.car.get_car_details() + "\nThin Rain Shield"


class CurvedRainShieldDecorator(CarDecorator):
    def __init__(self, car):
        self.car = car

    def get_car_price(self):
        return self.car.get_car_price() + 1500

    def get_car_details(self):
        return self.car.get_car_details() + "\nCurved Rain Shield"
