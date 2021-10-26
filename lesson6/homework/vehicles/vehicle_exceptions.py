class CargoWeightError(ValueError):

    def __init__(self, cargo_weight, weight):
        self.cargo_weight = cargo_weight
        self.weight = weight

    def __str__(self):
        return f'Cargo weight {self.cargo_weight}' \
               f' must not be greater than weight {self.weight}!'


class NoFuelError(Exception):

    def __str__(self):
        return f'Fuel tank is empty'


class EngineNotStartedError(Exception):

    def __str__(self):
        return f'Engine not started!'
