from lesson6.homework.vehicle_exceptions.engine_not_started_error import EngineNotStartedError
from lesson6.homework.vehicles.ice_vehicle import ICEVehicle
from lesson6.homework.vehicles.ice_vehicle_engine import ICEVehicleEngine


class TucsonVehicle(ICEVehicle):

    def __init__(self, name, weight, cargo_weight,
                 fuel_type, fuel_consumption,
                 tank_capacity, fuel_qnty, engine
                 # Cheap (chip) tuning! :)
                 , engine_auto_start
                 ):
        super().__init__(name, weight, cargo_weight, fuel_type,
                         fuel_consumption, tank_capacity, fuel_qnty,
                         engine
                         )
        self.engine_auto_start = engine_auto_start

    def beep(self):
        print('Beep-beep! :)')

    def __repr__(self):
        return f'{super().__repr__()}' \
               f',\nChip (cheap) tuning: engine autostart: {self.engine_auto_start}'

    # Adding chip tuning: engine autostart :)
    def go(self, kilometers):
        if not self._engine_started:
            if self.engine_auto_start:
                self.start_engine()
            else:
                raise EngineNotStartedError
        super().go(kilometers)


class CarVehicleTucsonJm(TucsonVehicle):

    def __init__(self, fuel_qnty):
        super().__init__('Tucson JM', 1800, 500, 'gasoline',
                         12, 60, fuel_qnty,
                         ICEVehicleEngine('G4GC', 2.0, 4, 6000),
                         True
                         )
