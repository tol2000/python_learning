# lecture 5 0:47

def dict_wo_dunder(dct: dict):
    dct1 = {}
    for key in dct.keys():
        if not (key.startswith("__") and key.endswith("__")):
            dct1[key] = dct[key]
    return dct1


def print_namespaces_with_parents(cls):
    for parent in cls.__bases__:
        if parent.__name__ != 'object':
            print_namespaces_with_parents(parent)
    print(f"{cls.__name__}: {dict_wo_dunder(cls.__dict__)}")


class MyMetaClass(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        print("New class", name)
        print("Bases", bases)
        print("Namespace", dict_wo_dunder(namespace))
        return super().__new__(mcs, name, bases, namespace, **kwargs)


class MyMetaClass1(MyMetaClass):
    def __new__(mcs, name, bases, namespace, **kwargs):
        print("New 1")
        return super().__new__(mcs, name, bases, namespace, **kwargs)


NewFoo = MyMetaClass('NewFoo', (), {"spam": "eggs"})


class NewFoo1(NewFoo):
    spam1 = 'eggs1'


class NewFoo2(NewFoo1, metaclass=MyMetaClass1):
    foo = 'bar'
    ba = 'for'


print("-------------------------------")
print_namespaces_with_parents(NewFoo2)
