class Car:
    def __init__(self):
        self._init_fuel = 50
        self.__fuel = None

    @property
    def fuel(self):
        print('Getting fuel...')
        if not self.__fuel:
            self.__fuel = self._init_fuel
        return self.__fuel

    @fuel.setter
    def fuel(self, value):
        print(f'Setting fuel to {value}...')
        self.__fuel = value


class Truck(Car):

    def __init__(self):
        super().__init__()
        # protected (_var) accessible from ancestor
        # but private (__var, e.g. __fuel) is not accessible from it
        self._init_fuel = 500
        print(f'Truck created with fuel: {self.fuel}')


c = Car()
print(f'Car fuel is: {c.fuel}')
c.fuel = 100
print(f'Car fuel is: {c.fuel}')

t = Truck()
print(f'Car fuel is: {t.fuel}')
t.fuel = 100
print(f'Car fuel is: {t.fuel}')
