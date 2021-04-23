#
class Test:
    instances = []
    x = 0

    def __init__(self):
        self.instances.append(id(self))
        self.x += 1
        print(f'self.instances = {self.instances}')
        print(f'self.x = {self.x}')
        print(f'Test.x = {Test.x}')


a = Test()
b = Test()
c = Test()
