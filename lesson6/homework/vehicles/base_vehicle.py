from abc import ABCMeta, abstractmethod

from lesson6.homework.vehicles.vehicle_exceptions import CargoWeightError


class BaseVehicle(metaclass=ABCMeta):

    def __init__(self, name, weight, cargo_weight):
        self.name = name
        self.weight = weight
        self.cargo_weight = cargo_weight

        if self.cargo_weight > self.weight:
            raise CargoWeightError

    def __repr__(self):
        return f'{self.name}, weight: {self.weight}, max cargo lift: {self.cargo_weight}'

    @abstractmethod
    def beep(self):
        """
        How vehicle sounds )
        :return:
        """
        raise NotImplementedError

    @abstractmethod
    def start_engine(self):
        """
        How vehicle starts its engine
        :return:
        """
        raise NotImplementedError
