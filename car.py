class Car:

    def __init__(self, init_fuel):
        self._fuel = init_fuel
        print(self, "created")

    def add_fuel(self, fuel_to_add):
        self._fuel += fuel_to_add

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, new_value):
        self._fuel = new_value

    def __str__(self):
        return f"car with fuel: {self.fuel}"


class Truck(Car):
    def __str__(self):
        return f"truck with fuel: {self.fuel}"


c = Car(100)
t = Truck(500)
t.fuel += 500
print(t)
