from notification_system import NotificationSystem  # Import the NotificationSystem class

class Subscriber:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def request_subscription(self):
        NotificationSystem.get_instance().add_subscriber(self)

    def update(self, update_info):
        print(f"Dear Customer {self.name} {update_info}")
