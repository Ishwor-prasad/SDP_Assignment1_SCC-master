class OpenRoofDecorator(CarDecorator):
    def __init__(self, car):
        self.car = car

    def get_car_price(self):
        return self.car.get_car_price() + 1000

    def get_car_details(self):
        return self.car.get_car_details() + "\nOpen Roof"
