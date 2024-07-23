import pytest

from backend.src.app import app
from src.components.engine import GasolineEngine, ElectricEngine, DieselEngine
from src.components.transmission import ManualTransmission, AutomaticTransmission
from src.factory.engine_factory import EngineFactory
from src.factory.transmission_factory import TransmissionFactory

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def gasoline_engine():
    return GasolineEngine()

@pytest.fixture
def electric_engine():
    return ElectricEngine()

@pytest.fixture
def diesel_engine():
    return DieselEngine()

@pytest.fixture
def manual_transmission():
    return ManualTransmission()

@pytest.fixture
def automatic_transmission():
    return AutomaticTransmission()

@pytest.fixture
def engine_factory():
    return EngineFactory

@pytest.fixture
def transmission_factory():
    return TransmissionFactory