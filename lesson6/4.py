class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def rurn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'speed {self.name} is {self.speed} km/h'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Speed of {self.name} is {self.speed}')
        if self.speed > 60:
            return f'{self.name} speeds up'
        else:
            return f'{self.name} observes speed limits'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def show_speed(self):
        print(f'Speed of {self.name} is {self.speed}')
        if self.speed > 40:
            return f'{self.name} speeds up'
        else:
            return f'{self.name} observes speed limits'

class PoliceCar(Car):
    def police(self):
        if self.is_police:
            return f'{self.name} is police car'
        else:
            return f'{self.name} is not police car'

opel = TownCar(70, 'white', 'Opel Astra GTC', False)
audi = SportCar(180, 'dark grey', 'Audi R8 V10', False)
ford = WorkCar (30, 'black', 'Ford Mondeo', False)
skoda = PoliceCar(170, 'metalic grey', 'Skoda Octavia A7', True)
print(opel.stop())
print(opel.color)
print(opel.show_speed())
print(opel.turn_right())
print(audi.show_speed())
print(f'{ford.go()}, next {ford.turn_right()} and work car {ford.stop()}')
print(ford.show_speed())
print(f'What the color this police car? - {skoda.color}')
print(skoda.is_police)