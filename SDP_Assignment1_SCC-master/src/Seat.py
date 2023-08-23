from abc import ABC, abstractmethod

class Seat(ABC):
    @abstractmethod
    def seat_type(self):
        pass

    @abstractmethod
    def get_seat_count(self):
        pass


class PrivateCarSeat(Seat):
    def seat_type(self):
        return "Private Car Seat"

    def get_seat_count(self):
        return 5


class RacingCarSeat(Seat):
    def seat_type(self):
        return "Racing Car Seat"

    def get_seat_count(self):
        return 1


class SUVCarSeat(Seat):
    def seat_type(self):
        return "SUV Seat"

    def get_seat_count(self):
        return 15


class MilitaryCarSeat(Seat):
    def seat_type(self):
        return "Military Car Seat"

    def get_seat_count(self):
        return 7
