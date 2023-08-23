from datetime import date
from central_online_system import CentralOnlineSystem
from command import RequestCarServicingCommand, RequestCarWashCommand, RequestOnlineDeliveryCommand
from mobile_adapter import MobileAdapter

class WebAdapter(MobileAdapter):
    def __init__(self):
        self.central_online_system = CentralOnlineSystem.get_instance()

    def request_car_servicing(self, name, date):
        command = RequestCarServicingCommand(name, date)
        self.central_online_system.add_command(command)

    def request_car_wash(self, name, date):
        command = RequestCarWashCommand(name, date)
        self.central_online_system.add_command(command)

    def request_online_delivery(self, name, date):
        command = RequestOnlineDeliveryCommand(name, date)
        self.central_online_system.add_command(command)
