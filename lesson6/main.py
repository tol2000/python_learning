import traceback

# Несколько способов импорта
# 1. весь модуль
import animals
# 2. весь модуль с псевдонимом
# import animals as an
# import numpy as np
# 3. конкретно то что нужно
# from animals import Bear, PositiveValueError
# from animals import Bear, PositiveValueError
# 4. всё - не рекомендуется
# from animals import *
# from _tkinter import *

# Импорт из модуля которые еще в папке (или в нескольких)
# from core.animals import Bear, PositiveValueError

# Модули и пакеты
from corepackage.animals import Bear, PositiveValueError
from corepackage import Bear, PositiveValueError


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
