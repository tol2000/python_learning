# def fu(v1=None):
#     if not getattr(fu, "v", None):
#         fu.v = v1
#     return fu.v
#
#
# print(fu())
# print(fu(5))
# print(fu())


class Foo:
    x = 'original'


o1, o2 = Foo(), Foo()
o1.x = 'changed'
# Foo.x = 'spam'

print(f'o1.x: {o1.x}')
print(f'o2.x: {o2.x}')
print(f'Foo.x: {Foo.x}')


class Eggs:
    x = 'Original'

    def __init__(self):
        Eggs.x = 'class changed'


Eggs.x = 'spam'
e1, e2 = Eggs(), Eggs()
e1.x = 'changed'

print(f'e1.x: {e1.x}')
print(f'e2.x: {e2.x}')
print(f'Eggs.x: {Eggs.x}')
