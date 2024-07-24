from src.components.car import Car
import logging

logger = logging.getLogger(__name__)


class CarBuilder:
    def __init__(self):
        self.car_id = None
        self.engine = None
        self.transmission = None

    def set_car_id(self, car_id):
        self.car_id = car_id
        logger.info(f"car {self} id set to: {car_id}")
        return self

    def set_engine(self, engine):
        self.engine = engine
        logger.info(f"car {self} engine set to: {self.engine.__class__.__name__}")
        return self

    def set_transmission(self, transmission):
        self.transmission = transmission
        logger.info(f"car {self} transmission set to: {self.transmission.__class__.__name__}")
        return self

    def build(self):
        if self.car_id and self.engine and self.transmission:
            return Car(self.car_id, self.engine, self.transmission)
        else:
            raise ValueError("Missing parts to build a car")
