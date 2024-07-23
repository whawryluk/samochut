from backend.src.components.engine import GasolineEngine, ElectricEngine, DieselEngine


def test_gasoline_engine():
    engine = GasolineEngine()
    assert engine.get_status() == "stopped"
    engine.start()
    assert engine.get_status() == "running"
    engine.stop()
    assert engine.get_status() == "stopped"


def test_electric_engine():
    engine = ElectricEngine()
    assert engine.get_status() == "stopped"
    engine.start()
    assert engine.get_status() == "running"
    engine.stop()
    assert engine.get_status() == "stopped"


def test_diesel_engine():
    engine = DieselEngine()
    assert engine.get_status() == "stopped"
    engine.start()
    assert engine.get_status() == "running"
    engine.stop()
    assert engine.get_status() == "stopped"
