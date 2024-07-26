import logging

from src.components.car_state_running import RunningState
from src.components.car_state_stopped import StoppedState


class Car:
    def __init__(self, car_id, engine, transmission):
        self.car_id = car_id
        self.engine = engine
        self.transmission = transmission

        self.logger = logging.getLogger(f'Car-{self.car_id}')

        self.stopped_state = StoppedState()
        self.running_state = RunningState()
        self.state = self.stopped_state

        self.logger.info(f'Car {self.car_id} created with initial state: {self.state.get_status()}')

    def set_state(self, state):
        self.state = state
        self.logger.info(f'Car {self.car_id} state changed to: {self.state.get_status()}')

    def start(self):
        self.state.start(self)
        if self.get_status() == "running":
            self.logger.info(f'Car {self.car_id} started')

    def stop(self):
        self.state.stop(self)
        if self.get_status() == "stopped":
            self.logger.info(f'Car {self.car_id} stopped')

    def get_status(self):
        return self.state.get_status()

    def to_dict(self):
        return {
            "car_id": self.car_id,
            "engine_type": self.engine.__class__.__name__,
            "transmission_type": self.transmission.__class__.__name__,
            "engine_status": self.engine.get_status(),
            "gear": self.transmission.get_gear()
        }

    def __repr__(self):
        return (f"Car(id={self.car_id}, "
                f"engine={self.engine.__class__.__name__}, "
                f"transmission={self.transmission.__class__.__name__}, "
                f"state={self.state.get_status()})")