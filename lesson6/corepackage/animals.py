class PositiveValueError(ValueError):

    def __init__(self, value, *args):
        self.value = value
        print(type(args))
        for item in args:
            print(item)

    def __str__(self):
        return f'Ваше число {self.value} отрицательно. А возраст не может быть меньше 0'


class Bear:

    def __init__(self, name, age):
        self.name = name

        if age < 0:
            # Исключение 1 - генерация
            # raise Exception('Возраст не может быть отрицательным')
            raise PositiveValueError(age, 1, 2, 3)
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'


# print(__name__)
if __name__ == '__main__':
    print('I am from animals')
