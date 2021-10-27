from lesson6.homework.vehicle_exceptions.no_power_error import NoPowerError
from lesson6.homework.vehicles.base_vehicle import BaseVehicle
from lesson6.homework.vehicles.tucson_vehicle import CarVehicleTucsonJm
from lesson6.homework.vehicles.sail_boat import SailBoat


def vehicle_go(vehicle: BaseVehicle, kilometers):
    """
    Demonstration of polymorphism
    """
    print('---------------------------------')
    print('Go!:')
    try:
        vehicle.go(kilometers)
    except NoPowerError as e:
        print('Error!', e)


if __name__ == '__main__':
    print('---------------------------------')
    my = CarVehicleTucsonJm(24)
    print(my)
    vehicle_go(my, 199)
    vehicle_go(my, 3)
    vehicle_go(my, 2)

    print('---------------------------------')
    captain_vrungel_yacht = SailBoat('Pobeda', 3000, 800, 3)
    print(captain_vrungel_yacht)
    vehicle_go(captain_vrungel_yacht, 10)
    vehicle_go(captain_vrungel_yacht, 5)
    vehicle_go(captain_vrungel_yacht, 50)
