from lesson6.homework.vehicle_exceptions.no_power_error import NoPowerError


class NoFuelError(NoPowerError):

    def __str__(self):
        return f'Fuel tank is empty'
