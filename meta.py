class MyMetaClass:
    def __new__(cls, name, bases, dct, *args, **kwargs):
        return super().__new__(cls, name, bases, dct, *args, **kwargs)
