from abc import ABC, abstractmethod

class AutomatedAI(ABC):
    @abstractmethod
    def get_region(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass


class AsiaAutomatedAI(AutomatedAI):
    def get_region(self):
        return "Asia"

    def get_cost(self):
        return 1000


class USAAutomatedAI(AutomatedAI):
    def get_region(self):
        return "USA"

    def get_cost(self):
        return 2000
