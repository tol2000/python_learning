class Solver:
    @classmethod
    def add(cls, a, b):
        res = a + b
        if divmod(a, 2)[1] == 0:
            res = res + 1
        # print("res:", res)
        return res


def mul(a, b):
    return a * b


SUB_ERROR_TEXT = "All arguments have to be int or float"


def sub(a, b):
    if not all(
        map(
            lambda v: isinstance(v, (int, float)),
            (a, b),
        )
    ):
        raise TypeError(SUB_ERROR_TEXT)
    return a - b
