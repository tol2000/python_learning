class CargoWeightError(ValueError):

    def __init__(self, cargo_weight, weight):
        self.cargo_weight = cargo_weight
        self.weight = weight

    def __str__(self):
        return f'Cargo weight {self.cargo_weight}' \
               f' must not be greater than weight {self.weight}!'
