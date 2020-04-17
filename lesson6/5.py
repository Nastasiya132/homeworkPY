class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'You started drawning'

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'You took {self.title}. Started drawning pen'

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'You took {self.title}. Started drawning pencil'

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f'You took {self.title}. Started drawning handle'

red_pen = Pen('Red pen')
graphite_pencil = Pencil('Graphite pencil')
green_handle = Handle('Green handle')
print(red_pen.draw())
print(graphite_pencil.draw())
print(green_handle.draw())