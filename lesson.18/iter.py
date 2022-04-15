class Tol:
    def __init__(self, name):
        self.name = name
        self.index = 0
        self.index2stop = len(self.name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.index2stop:
            result = self.name[self.index]
            self.index += 1
        else:
            raise StopIteration
        return result

    # def __getitem__(self, item):
    #     return self.name[item]


obj = Tol('Tolic.mac')

# print(obj[2], '\n')

for letter in obj:
    print(letter)
print()

obj = Tol('Tolic.mac')
print(sorted(obj)[-1])
