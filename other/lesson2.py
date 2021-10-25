import os
from functools import wraps

# Some decoration (shadowing) of standard function print to learn decoration
# It will be logging all prints while log is true :)

log = []
to_log: bool


def print_decor(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if to_log:
            global log
            if args.__ne__(None):
                log += args
            if kwargs.__ne__(None):
                log += [{x: kwargs[x]} for x in kwargs.keys()]
            return f(end="")
        else:
            return f(*args, **kwargs)
    return wrapper


print = print_decor(print)


def recurcive_dir(dir_name, level=0):
    os_dir = os.listdir(dir_name)
    for loc_item in os_dir:
        f_name = dir_name+os.path.sep+loc_item
        indent = '     ' * level
        if os.path.isdir(f_name):
            yield f'{indent}Dir: {f_name}'
            for loc_list_item in list(recurcive_dir(f_name, level+1)):
                yield loc_list_item
        else:
            yield f'{indent}{f_name}'


to_log = True

print('\n\nHello! It is my recurcive directory list generator!', "It will be cool! :)")
print(begin="true")
print()
names = list(recurcive_dir('/home/tolic/tol/bat'))
for item in names:
    print(item)
print(end="true")

to_log = False

print("\n\nLog contents:")
print("-----------------------------------")
for s in log:
    print(s)
