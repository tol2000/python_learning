from lesson6.homework.vehicles.ice_vehicle import ICEVehicle


class CarVehicle(ICEVehicle):

    def __init__(self, name, weight, cargo_weight,
                 fuel_type, fuel_consumption,
                 tank_capacity, fuel_qnty, wheels
                 ):
        super().__init__(name, weight, cargo_weight, fuel_type,
                         fuel_consumption, tank_capacity, fuel_qnty
                         )
        self.wheels = wheels

    def beep(self):
        print('Beep-beep! :)')


class CarVehicleTucsonJm(CarVehicle):

    def __init__(self, fuel_qnty):
        super().__init__('Tucson JM', 1800, 500, 'gasoline', 12, 60, fuel_qnty, 4)
