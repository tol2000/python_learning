from abc import ABCMeta

from lesson6.homework.vehicles.base_vehicle import BaseVehicle


class EcoVehicle(BaseVehicle, metaclass=ABCMeta):

    def __init__(self, name, weight, cargo_weight,
                 kind_of_eco_energy
                 ):
        self.kind_of_eco_energy = kind_of_eco_energy
        super().__init__(name, weight, cargo_weight)

    def __repr__(self):
        return f'{super().__repr__()}' \
               f', power of nature: {self.kind_of_eco_energy}'
