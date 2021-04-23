#
class Test:
    instances = []
    x = 5

    def __init__(self):
        self.instances.append(id(self))
        self.x = 6
        print(f'self.instances = {self.instances}')
        print(f'Test.instances = {self.instances}')
        print(f'Test.x = {Test.x}')
        print(f'self.x = {self.x}')


a = Test()
b = Test()
c = Test()
