from src.components.engine import GasolineEngine, ElectricEngine, DieselEngine

class EngineFactory:
    @staticmethod
    def create_engine(engine_type: str):
        if engine_type == "GasolineEngine":
            return GasolineEngine()
        elif engine_type == "ElectricEngine":
            return ElectricEngine()
        elif engine_type == "DieselEngine":
            return DieselEngine()
        else:
            raise ValueError(f"Unknown engine type {engine_type}")
