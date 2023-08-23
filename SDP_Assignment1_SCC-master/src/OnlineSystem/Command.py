from datetime import date

class Command:
    def execute(self):
        pass  # Implement the command execution logic

    def get_date(self):
        pass  # Implement the method to get the command date


class RequestCarServicingCommand(Command):
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def execute(self):
        print(f"Requesting car servicing for {self.name} on {self.date}")

    def get_date(self):
        return self.date


class RequestCarWashCommand(Command):
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def execute(self):
        print(f"Requesting car wash for {self.name} on {self.date}")

    def get_date(self):
        return self.date


class RequestOnlineDeliveryCommand(Command):
    def __init__(self, name, date):
        self.name = name
        self.date = date

    def execute(self):
        print(f"Requesting online delivery for {self.name} on {self.date}")

    def get_date(self):
        return self.date
