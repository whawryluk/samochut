from abc import ABC, abstractmethod


class Transmission(ABC):
    @abstractmethod
    def shift_up(self):
        pass

    @abstractmethod
    def shift_down(self):
        pass

    @abstractmethod
    def get_gear(self):
        pass


class ManualTransmission(Transmission):
    def __init__(self):
        self.gear = 1

    def shift_up(self):
        self.gear += 1

    def shift_down(self):
        if self.gear > 1:
            self.gear -= 1

    def get_gear(self):
        return self.gear


class AutomaticTransmission(Transmission):
    def __init__(self):
        self.gear = 1

    def shift_up(self):
        self.gear += 1

    def shift_down(self):
        if self.gear > 1:
            self.gear -= 1

    def get_gear(self):
        return self.gear
