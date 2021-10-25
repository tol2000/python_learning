class PositiveValueError(ValueError):

    def __init__(self, value, *args):
        self.value = value
        print(type(args))
        for item in args:
            print(item)

    def __str__(self):
        return f'Ваше число {self.value} отрицательно. А возраст не может быть меньше 0'