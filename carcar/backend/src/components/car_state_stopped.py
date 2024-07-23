from .car_state import CarState

class StoppedState(CarState):
    def start(self, car):
        car.logger.info("Starting the car.")
        if car.engine.get_status() == "stopped" and car.transmission.get_gear() in ["neutral", "park"]:
            car.engine.start()
            car.set_state(car.running_state)
        else:
            car.logger.info("Cannot start the car. Ensure the engine is off and the gear is in neutral or park.")

    def stop(self, car):
        car.logger.info("The car is already stopped.")

    def get_status(self):
        return "stopped"
