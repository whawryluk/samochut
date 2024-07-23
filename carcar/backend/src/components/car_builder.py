from .car import Car

class CarBuilder:
    def __init__(self):
        self.car_id = None
        self.engine = None
        self.transmission = None

    def set_car_id(self, car_id):
        self.car_id = car_id
        return self

    def set_engine(self, engine):
        self.engine = engine
        return self

    def set_transmission(self, transmission):
        self.transmission = transmission
        return self

    def build(self):
        if self.car_id and self.engine and self.transmission:
            return Car(self.car_id, self.engine, self.transmission)
        else:
            raise ValueError("Missing parts to build a car")