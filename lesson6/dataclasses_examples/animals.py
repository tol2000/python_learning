from errors import PositiveValueError
from dataclasses import dataclass
from food import Food


# class Bear:
#
#     def __init__(self, name, age, food):
#         self.food = food
#         self.name = name
#
#         if age < 0:
#             # Исключение 1 - генерация
#             # raise Exception('Возраст не может быть отрицательным')
#             raise PositiveValueError(age, 1, 2, 3)
#         self.age = age
#
#     def __str__(self):
#         return f'{self.name} {self.age}'

@dataclass
class Bear:
    name: str
    age: int
    food: Food

    def __post_init__(self):
        if self.age < 0:
            raise PositiveValueError(self.age, 1, 2, 3)


# print(__name__)
if __name__ == '__main__':
    bear = Bear('Фауст', -20, Food('', ''))
