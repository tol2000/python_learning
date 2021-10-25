import traceback


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


name = 'Фауст'
age = int(input('Введите возраст'))

# 2. Обработка исключений
try:
    bear = Bear(name, age)
    # 5/0
except PositiveValueError as e:
    # Была ошибка
    print('Была ошибка', e)
    # print('Была ошибка', traceback.format_exc())
except ValueError:
    print('Ошибка в числе')
except Exception:
    print('Что то пошло не так?')
else:
    # Ошибки не было
    print('Медведь создан')
    print(bear)
finally:
    # Выпонить в любом случае была или не была
    print('end')
