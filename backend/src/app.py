import logging

from flask import Flask, jsonify, request
from .config import setup_logging

from src.components.car_builder import CarBuilder
from src.factory.engine_factory import EngineFactory
from src.factory.transmission_factory import TransmissionFactory

setup_logging()
logger = logging.getLogger(__name__)

logger.info("Starting Flask application...")

app = Flask(__name__)

cars = {}

logger.info("Flask application setup complete.")


@app.route('/api/cars', methods=['POST'])
def create_car():
    logger.info("Received request to create a car")
    data = request.get_json()
    car_id = data.get("id")
    engine_type = data.get("engine_type")
    transmission_type = data.get("transmission_type")
    logger.info("TIBIA")
    logger.info(f"car_id: {car_id}")
    logger.info(f"engine_type: {engine_type}")
    logger.info(f"transmission_type: {transmission_type}")

    if car_id in cars:
        return jsonify({
            "error": f"Car with ID {car_id} already exists"
        }), 400

    engine = EngineFactory.create_engine(engine_type)
    transmission = TransmissionFactory.create_transmission(transmission_type)
    car_builder = CarBuilder()

    currcarr = (car_builder
                .set_car_id(car_id)
                .set_engine(engine)
                .set_transmission(transmission)
                .build())

    cars[car_id] = currcarr

    return jsonify({
        "message": f"Car {car_id} with {engine_type.replace("Engine", "").lower()}"
                   f" engine and {transmission_type.replace("Transmission", "").lower()} transmission created"
    }), 201


@app.route('/api/cars', methods=['GET'])
def get_cars():
    logger.info("Received request to get all cars")
    car_list = [car.to_dict() for car_id, car in cars.items()]
    return jsonify(car_list), 200


@app.route('/api/cars/<car_id>', methods=['GET'])
def get_car(car_id):
    logger.info(f"Received request to get car with ID {car_id}")
    car = cars.get(car_id)
    if not car:
        return jsonify({"error": "Car not found"}), 404
    return jsonify(car.to_dict()), 200


@app.route('/api/cars/<car_id>/start', methods=['POST'])
def start_car(car_id):
    logger.info(f"Received request to start car with ID {car_id}")
    if car_id in cars:
        cars[car_id].start()
        return jsonify({"message": f"Car {car_id} engine started"}), 200
    return jsonify({"error": "Car not found"}), 404


@app.route('/api/cars/<car_id>/stop', methods=['POST'])
def stop_car(car_id):
    logger.info(f"Received request to stop car with ID {car_id}")
    if car_id in cars:
        cars[car_id].stop()
        return jsonify({"message": f"Car {car_id} engine stopped"}), 200
    return jsonify({"error": "Car not found"}), 404


@app.route('/api/cars/<car_id>/shift_up', methods=['POST'])
def shift_up(car_id):
    logger.info(f"Received request to shift up car with ID {car_id}")
    car = cars.get(car_id)
    if car:
        car.transmission.shift_up()
        return jsonify({"message": f"Car {car_id} gear up"}), 200
    return jsonify({"error": "Car not found"}), 404


@app.route('/api/cars/<car_id>/shift_down', methods=['POST'])
def shift_down(car_id):
    logger.info(f"Received request to shift down car with ID {car_id}")
    car = cars.get(car_id)
    if car:
        car.transmission.shift_down()
        return jsonify({"message": f"Car {car_id} gear down"}), 200
    return jsonify({"error": "Car not found"}), 404


if __name__ == '__main__':
    logger.info("Flask application setup complete.")
    app.run(debug=True)
