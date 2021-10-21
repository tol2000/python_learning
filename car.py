class Car:

    def __init__(self, init_fuel):
        self._fuel = init_fuel
        print(self, "created")

    def add_fuel(self, fuel_to_add):
        self._fuel += fuel_to_add

    def get_fuel(self):
    #     1:20

    def __str__(self):
        return f"car with fuel: {self._fuel}"


class Truck(Car):
    def __str__(self):
        return f"truck with fuel: {self._fuel}"


c = Car(100)
t = Truck(500)
print(c._fuel)
