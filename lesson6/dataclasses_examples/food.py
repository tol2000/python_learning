from dataclasses import dataclass


# class Food:
#
#     def __init__(self, name, food_type):
#         self.name = name
#         self.food_type = food_type

@dataclass(frozen=True)
class Food:
    name: str
    food_type: str


if __name__ == '__main__':
    food = Food('мёд', 'сладкое')
    print(food)

    food1 = Food('мёд', 'сладкое')

    print(food == food1)
