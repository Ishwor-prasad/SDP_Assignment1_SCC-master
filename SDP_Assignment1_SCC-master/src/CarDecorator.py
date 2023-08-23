from car import Car  # Assuming you have a Car class defined

class CarDecorator(Car):
    def __init__(self, car):
        self.car = car

    def get_car_price(self):
        pass  # Implement in derived decorators

    def get_car_details(self):
        pass  # Implement in derived decorators
