from lesson6.homework.vehicle_exceptions.no_power_error import NoPowerError


class NoWindError(NoPowerError):

    def __str__(self):
        return f'There is no wind, Calm! )'
