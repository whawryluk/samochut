from components.engine import GasolineEngine, ElectricEngine, DieselEngine

class EngineFactory:
    @staticmethod
    def create_engine(engine_type: str):
        if engine_type == "gasoline":
            return GasolineEngine()
        elif engine_type == "electric":
            return ElectricEngine()
        elif engine_type == "diesel":
            return DieselEngine()
        else:
            raise ValueError(f"Unknown engine type {engine_type}")
