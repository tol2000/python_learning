from abc import ABCMeta

from lesson6.homework.vehicles.base_vehicle import BaseVehicle
from lesson6.homework.vehicles.vehicle_exceptions import \
     EngineNotStartedError, NoFuelError


class ICEVehicle(BaseVehicle, metaclass=ABCMeta):

    def __init__(self, name, weight, cargo_weight,
                 fuel_type, fuel_consumption,
                 tank_capacity, fuel_qnty,
                 ):
        """

        :param name:
        :param weight:
        :param cargo_weight:
        :param fuel_type:
        :param fuel_consumption: liters on 100km
        :param tank_capacity:
        :param fuel_qnty:
        """
        super().__init__(name, weight, cargo_weight)

        self.fuel_type = fuel_type
        self.fuel_consumption = fuel_consumption
        self.tank_capacity = tank_capacity
        self.fuel_qnty = fuel_qnty

        self._engine_started = False

    def __repr__(self):
        return f'{super().__repr__()}' \
               f', fuel type: {self.fuel_type}' \
               f', fuel consumption: {self.fuel_consumption}' \
               f', tank capacity: {self.tank_capacity}' \
               f', fuel quantity: {self.fuel_qnty}'

    def start_engine(self):
        if self.fuel_qnty <= 0:
            raise NoFuelError
        else:
            self._engine_started = True
            print(f'{self.name}: engine started!')

    def stop_engine(self):
        self._engine_started = False
        print(f'{self.name}: engine stopped!')

    def go(self, kilometers):
        if not self._engine_started:
            raise EngineNotStartedError
        fuel = (kilometers * self.fuel_consumption) / 100
        if fuel >= self.fuel_qnty:
            self.fuel_qnty -= fuel
            print(f'Successfully drove {kilometers} kilometers')
        else:
            self.fuel_qnty = 0
            print(f'Drove less kilometers than planned because of empty fuel!')
        if self.fuel_qnty == 0:
            self.stop_engine()
