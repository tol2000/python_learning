import os


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


print('\n\nHello! It is my recurcive directory list generator!')
names = list(recurcive_dir('/home/tolic/tol/bat'))
for item in names:
    print(item)
