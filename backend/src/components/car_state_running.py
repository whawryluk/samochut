from src.components.car_state import CarState


class RunningState(CarState):
    def start(self, car):
        car.logger.info("The car is already running.")

    def stop(self, car):
        car.logger.info("Stopping the car..")
        if car.engine.get_status() == "running":
            car.engine.stop()
            car.set_state(car.stopped_state)
            car.logger.info("Car stopped successfully.")
        else:
            car.logger.info("Cannot stop the car. The engine is already stopped.")

    def get_status(self):
        return "running"
