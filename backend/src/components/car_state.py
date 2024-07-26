from abc import ABC, abstractmethod


class CarState(ABC):
    @abstractmethod
    def start(self, car):
        pass

    @abstractmethod
    def stop(self, car):
        pass

    @abstractmethod
    def get_status(self):
        pass
