class Road:
    def __init__(self, _lenght, _widht, weight, thickness):
        self._lenght = _lenght
        self._widht = _widht
        self.weight = weight
        self.thickness = thickness

    def weight_road(self):
        weight_road = self._lenght * self._widht * self.weight * self.thickness / 1000
        print(weight_road)


weight_for_you = Road(20, 5000, 25, 5)
weight_for_you.weight_road()
