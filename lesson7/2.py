class Clothes:
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_coat(self):
        return self.size / 6.5 + 0.5

    def get_costume(self):
        return 2 * self.height + 0.3

    @property
    def get_all(self):
        return f'На все изделия потребуется ткани: {(self.size / 6.5 + 0.5) + (2 * self.height + 0.3)}'


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.cloth_coat = self.size / 6.5 + 0.5

    def __str__(self):
        return f'Расход ткани на пальто: {self.cloth_coat}м'

class Costume(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.cloth_costume = 2 * self.height + 0.3

    def __str__(self):
        return f'Расход ткани на костюм {self.cloth_costume}м'


coat = Coat(5, 3)
costume = Costume(4, 5)
print(coat)
print(coat.get_coat())
print(coat.get_all)
print(costume)
print(costume.get_costume())
print(costume.get_all)

