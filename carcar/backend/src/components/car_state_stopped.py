from src.components.car_state import CarState


class StoppedState(CarState):
    def start(self, car):
        car.logger.info("Starting the car.")
        car.logger.info(f"car status: {car.engine.get_status()}")
        car.logger.info(f"car gear: {car.transmission.get_gear()}, {type(car.transmission.get_gear())}")
        if car.engine.get_status() == "stopped" and car.transmission.get_gear() in ["neutral", "park", 1]:
            car.engine.start()
            car.set_state(car.running_state)
            car.logger.info("Car started successfully.")
        else:
            car.logger.info("Cannot start the car. Ensure the engine is off and the gear is in neutral or park.")

    def stop(self, car):
        car.logger.info("The car is already stopped.")

    def get_status(self):
        return "stopped"
