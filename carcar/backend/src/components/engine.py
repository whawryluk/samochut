from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def get_status(self):
        pass


class GasolineEngine(Engine):
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def get_status(self):
        return "running" if self.running else "stopped"


class ElectricEngine(Engine):
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def get_status(self):
        return "running" if self.running else "stopped"


class DieselEngine(Engine):
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True

    def stop(self):
        self.running = False

    def get_status(self):
        return "running" if self.running else "stopped"
