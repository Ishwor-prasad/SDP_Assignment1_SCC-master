class Subscriber:
    def update(self, message):
        pass  # Implement the update logic


class NotificationSystem:
    def __init__(self):
        self.subscriber_list = []
        self.notification_system = None

    @classmethod
    def get_instance(cls):
        if cls.notification_system is None:
            cls.notification_system = cls()
        return cls.notification_system

    def add_subscriber(self, subscriber):
        self.subscriber_list.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscriber_list.remove(subscriber)

    def notify_price_change(self):
        for subscriber in self.subscriber_list:
            subscriber.update("Price has changed")

    def notify_feature_change(self):
        for subscriber in self.subscriber_list:
            subscriber.update("Feature has changed")
