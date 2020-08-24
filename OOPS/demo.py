class Computer:
    def __init__(self, cpu, ram):

        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("{}, {}gb ram  and 1tb ssd".format(self.cpu, self.ram))


com1 = Computer('i5', 12)
com2 = Computer('i7', 16)

Computer.config(com1)
Computer.config(com2)
