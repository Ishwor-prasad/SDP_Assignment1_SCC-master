from NotifierSubscriber import NotificationSystem, Subscriber
from CarFactory import RacingCarFactory, PrivateCarFactory, FordUSA
from CarDecorator import OpenRoofDecorator, LoosenBigBumperDecorator, CurvedRainShieldDecorator
from CarShop import CarType

def main():
    # CarFactory test
    print(" ___________________ Testing CarFactory ___________________")
    car_factory = RacingCarFactory()
    car = car_factory.create_car("Red", "Asia", "Ford")
    print(car.get_car_details())
    
    car_factory = PrivateCarFactory()
    car = car_factory.create_car("White", "Asia", "Ford")
    print(car.get_car_details())
    
    # CarShop test
    print(" ___________________ Testing CarShop ___________________")
    car_shop1 = FordUSA()
    car1 = car_shop1.order_car("Red", CarType.RACING)
    car2 = car_shop1.order_car("White", CarType.SUV)
    car3 = car_shop1.order_car("Black", CarType.PRIVATE)
    print(car1.get_car_details())
    print(car2.get_car_details())
    print(car3.get_car_details())
    
    # CarDecorator test
    print(" ___________________ Testing CarDecorator ___________________")
    car_shop2 = FordUSA()
    car = car_shop2.order_car("Red", CarType.RACING)
    car = OpenRoofDecorator(car)
    car = LoosenBigBumperDecorator(CurvedRainShieldDecorator(car))
    print(car.get_car_details())
    
    # Online System test
    print(" ___________________ Testing Online System ___________________")
    
    # Test notification system
    notification_system = NotificationSystem.get_instance()
    print("Adding subscriber", "John")
    notification_system.add_subscriber(Subscriber("John", "jhon@mailmail.com"))
    print("Adding subscriber", "Mary")
    notification_system.add_subscriber(Subscriber("Mary", "mary@mailmail.com"))
    print("Adding subscriber", "Peter")
    notification_system.add_subscriber(Subscriber("Peter", "mailmail.com@mail"))
    
    print("Notify price change")
    notification_system.notify_price_change()
    print("Notify feature change")
    notification_system.notify_feature_change()

if __name__ == "__main__":
    main()
