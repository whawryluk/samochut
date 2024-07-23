from flask import Flask, jsonify, request

from components.car_builder import CarBuilder
from factory.engine_factory import EngineFactory
from factory.transmission_factory import TransmissionFactory

app = Flask(__name__)

cars = {}


@app.route('/api/cars', methods=['POST'])
def create_car():
    data = request.get_json()
    car_id = data.get("id")
    engine_type = data.get("engine_type")
    transmission_type = data.get("transmission_type")

    if car_id in cars:
        return jsonify({
            "error": f"Car with ID {car_id} already exists"
        }), 400

    engine = EngineFactory.create_engine(engine_type)
    transmission = TransmissionFactory.create_transmission(transmission_type)

    car_builder = CarBuilder()
    car = car_builder.set_car_id(car_id).set_engine(engine).set_transmission(transmission).build()
    cars[car_id] = car

    return jsonify({
        "message": f"Car {car_id} with {engine_type} engine and {transmission_type} transmission created"
    }), 201


@app.route('/api/cars', methods=['GET'])
def get_cars():
    car_list = [{"id": car_id, "engine_type": car.engine.__class__.__name__,
                 "transmission_type": car.transmission.__class__.__name__} for car_id, car in cars.items()]
    return jsonify(car_list), 200


@app.route('/api/cars/<car_id>', methods=['GET'])
def get_car(car_id):
    car = cars.get(car_id)
    if not car:
        return jsonify({"error": "Car not found"}), 404
    return jsonify({
        'car_id': car.car_id,
        'engine_status': car.engine.get_status(),
        'gear': car.transmission.get_gear()
    }), 200


@app.route('/api/cars/<car_id>/start', methods=['POST'])
def start_car(car_id):
    if car_id in cars:
        cars[car_id].engine.start()
        return jsonify({"message": f"Car {car_id} engine started"}), 200
    return jsonify({"error": "Car not found"}), 404


@app.route('/api/cars/<car_id>/stop', methods=['POST'])
def stop_car(car_id):
    if car_id in cars:
        cars[car_id].engine.stop()
        return jsonify({"message": f"Car {car_id} engine stopped"}), 200
    return jsonify({"error": "Car not found"}), 404


@app.route('/api/cars/<car_id>/shift_up', methods=['POST'])
def shift_up(car_id):
    if car_id in cars:
        cars[car_id].transmission.shift_up()
        return jsonify({"message": f"Car {car_id} shifted up"}), 200
    return jsonify({"error": "Car not found"}), 404


@app.route('/api/cars/<car_id>/shift_down', methods=['POST'])
def shift_down(car_id):
    if car_id in cars:
        cars[car_id].transmission.shift_down()
        return jsonify({"message": f"Car {car_id} shifted down"}), 200
    return jsonify({"error": "Car not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
