from src.components.transmission import ManualTransmission, AutomaticTransmission

class TransmissionFactory:
    @staticmethod
    def create_transmission(transmission_type: str):
        if transmission_type == "ManualTransmission":
            return ManualTransmission()
        elif transmission_type == "AutomaticTransmission":
            return AutomaticTransmission()
        else:
            raise ValueError(f"Unknown transmission type {transmission_type}")