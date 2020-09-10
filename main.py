# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hail, {name}!')  # Press Ctrl+8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Tolic')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

array = [1,2,3,4,5,6,7]

looping = True

while len(array) > 0:
    popa = array.pop(0)
    if popa != None:
        print(popa)
    else:
        looping = False

