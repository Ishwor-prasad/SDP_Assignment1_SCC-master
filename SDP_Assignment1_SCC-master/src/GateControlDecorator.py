class RemoteGateControlDecorator(CarDecorator):
    def __init__(self, car):
        self.car = car

    def get_car_price(self):
        return self.car.get_car_price() + 1000

    def get_car_details(self):
        return self.car.get_car_details() + "\nRemote Gate Control"


class MobileAppGateControlDecorator(CarDecorator):
    def __init__(self, car):
        self.car = car

    def get_car_price(self):
        return self.car.get_car_price() + 500

    def get_car_details(self):
        return self.car.get_car_details() + "\nMobile App Gate Control"
