from lesson6.homework.vehicle_exceptions.no_wind_error import NoWindError
from lesson6.homework.vehicles.eco_vehicle import EcoVehicle
from lesson6.homework.weather.wind import Wind


class SailBoat(EcoVehicle):

    def beep(self):
        print('To-too!')

    def go(self, kilometers):
        if Wind.if_wind():
            print(f'The {self.name} is sailing!')
        else:
            raise NoWindError

    def __init__(self, name, weight, cargo_weight,
                 num_of_sails
                 ):
        self.num_of_sails = num_of_sails
        super().__init__(name, weight, cargo_weight, 'Wind')
