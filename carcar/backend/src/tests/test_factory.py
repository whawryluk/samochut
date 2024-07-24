import pytest

from backend.src.factory.engine_factory import EngineFactory
from backend.src.factory.transmission_factory import TransmissionFactory


@pytest.fixture
def engine_factory():
    return EngineFactory


@pytest.fixture
def transmission_factory():
    return TransmissionFactory


def test_create_gasoline_engine(engine_factory, gasoline_engine):
    engine = engine_factory.create_engine("gasoline")
    assert type(engine) is type(gasoline_engine)


def test_create_electric_engine(engine_factory, electric_engine):
    engine = engine_factory.create_engine("electric")
    assert type(engine) is type(electric_engine)


def test_create_diesel_engine(engine_factory, diesel_engine):
    engine = engine_factory.create_engine("diesel")
    assert type(engine) is type(diesel_engine)


def test_create_unknown_engine(engine_factory):
    with pytest.raises(ValueError):
        engine_factory.create_engine("unknown")


def test_create_manual_transmission(transmission_factory, manual_transmission):
    transmission = transmission_factory.create_transmission("manual")
    assert type(transmission) is type(manual_transmission)


def test_create_automatic_transmission(transmission_factory, automatic_transmission):
    transmission = transmission_factory.create_transmission("automatic")
    assert type(transmission) is type(automatic_transmission)


def test_create_unknown_transmission(transmission_factory):
    with pytest.raises(ValueError):
        transmission_factory.create_transmission("unknown")
