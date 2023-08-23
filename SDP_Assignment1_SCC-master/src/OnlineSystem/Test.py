from datetime import date
from central_online_system import CentralOnlineSystem
from command import RequestCarServicingCommand, RequestCarWashCommand, RequestOnlineDeliveryCommand

if __name__ == "__main__":
    central_online_system = CentralOnlineSystem.get_instance()
    print(" ___________________ Testing Online System ___________________")
    
    command = RequestCarServicingCommand("Akib", date(2021, 5, 10))
    central_online_system.add_command(command)
    
    command = RequestCarServicingCommand("Rahim", date(2021, 5, 10))
    central_online_system.add_command(command)
    
    command = RequestCarWashCommand("Karim", date(2021, 5, 10))
    central_online_system.add_command(command)
    
    command = RequestOnlineDeliveryCommand("Rahim", date(2021, 5, 10))
    central_online_system.add_command(command)
    
    central_online_system.process_command()
