from animals import Bear
from zoo import Zoo
from food import Food

food = Food('Мёд', 'сладкое')

bear = Bear('Фауст', 5, food)

# zoo = Zoo([bear])
# zoo = Zoo([])
zoo = Zoo()

zoo.animals.append(bear)

print(zoo)
print(zoo.animals)
