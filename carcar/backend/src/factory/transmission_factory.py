from components.transmission import ManualTransmission, AutomaticTransmission

class TransmissionFactory:
    @staticmethod
    def create_transmission(transmission_type: str):
        if transmission_type == "manual":
            return ManualTransmission()
        elif transmission_type == "automatic":
            return AutomaticTransmission()
        else:
            raise ValueError(f"Unknown transmission type {transmission_type}")