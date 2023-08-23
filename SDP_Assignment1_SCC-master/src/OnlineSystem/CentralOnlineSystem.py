from datetime import date
from queue import Queue

class Command:
    def __init__(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def execute(self):
        pass  # Implement the command execution logic


class CentralOnlineSystem:
    central_online_system = None

    def __init__(self):
        self.command_queue = Queue()
        self.servicing_dates = []

    @classmethod
    def get_instance(cls):
        if cls.central_online_system is None:
            cls.central_online_system = cls()
        return cls.central_online_system

    def add_command(self, command):
        self.command_queue.put(command)
        self.servicing_dates.append(command.get_date())

    def process_command(self):
        while not self.command_queue.empty():
            command = self.command_queue.get()
            command.execute()
