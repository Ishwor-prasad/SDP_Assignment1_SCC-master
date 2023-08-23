class PrivateCar(Car):
    def __init__(self, engine, tire, chassis, ac, color, body_design, automated_ai, seat):
        self.engine = engine
        self.tire = tire
        self.chassis = chassis
        self.ac = ac
        self.color = color
        self.body_design = body_design
        self.automated_ai = automated_ai
        self.seat = seat

    def get_car_price(self):
        return (
            self.engine.get_engine_price()
            + self.tire.get_tire_price()
            + self.chassis.get_chassis_price()
            + self.ac.get_ac_price()
            + self.color.get_color_price()
            + self.body_design.get_body_design_price()
            + self.automated_ai.get_cost()
        )

    def get_car_details(self):
        return (
            "Private Car Details: "
            + self.engine.get_engine_type()
            + ", "
            + self.tire.get_tire_type()
            + ", "
            + self.chassis.get_chassis_type()
            + ", "
            + self.ac.get_ac_type()
            + ", "
            + self.color.get_color_type()
            + ", "
            + self.body_design.get_body_design_type()
            + ", "
            + self.automated_ai.get_region()
            + ", "
            + self.seat.seat_type()
        )
