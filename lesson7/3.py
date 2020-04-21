class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'{self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Result negative')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, in_row):
        row = ''
        for i in range(int(self.quantity / in_row)):
            row += f'{"*" * in_row} \\n'
        row += f'Result {"*" * (self.quantity % in_row)}'
        return row




cells1 = Cell(10)
cells2 = Cell(5)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(15))
print(cells1.make_order(5))
print(cells1 / cells2)