import pytest
import logging
from backend.src.components.car import Car
from backend.src.config import setup_logging

setup_logging()


@pytest.fixture
def car():
    return Car(car_id="test_car")


def test_initial_state(car):
    assert car.get_status() == "stopped"


def test_start_car(car, caplog):
    with caplog.at_level(logging.INFO):
        car.start()
        assert car.get_status() == "running"
        assert "Car test_car started" in caplog.text


def test_stop_car(car, caplog):
    with caplog.at_level(logging.INFO):
        car.start()
        assert car.get_status() == "running"
        car.stop()
        assert car.get_status() == "stopped"
        assert "Car test_car stopped" in caplog.text


def test_start_car_when_running(car, caplog):
    with caplog.at_level(logging.INFO):
        car.start()
        car.start()
        assert car.get_status() == "running"
        assert "The car is already running." in caplog.text


def test_stop_car_when_stopped(car, caplog):
    with caplog.at_level(logging.INFO):
        car.stop()
        car.stop()
        assert car.get_status() == "stopped"
        assert "The car is already stopped." in caplog.text
