class Computer:
    def __init__(self):
        self.name = 'gunjan'
        self.age = 20

    def details(self):
        print("name {} age {}".format(self.name, self.age))

    def update(self):
        self.age = 40

    def compare(Self, other):
        if(Self.age == other.age):
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()


if c1.compare(c2):
    print('same')

c2.update()
c2.details()
print(id(c1))
print(id(c2))
