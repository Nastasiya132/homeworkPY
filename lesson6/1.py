import time

class TrafficLight:
    __colors = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'{TrafficLight.__colors[i]}')
            if i == 0:
                time.sleep(7)
            elif i == 1:
                time.sleep(2)
            elif i == 2:
                time.sleep(1)
            i += 1

traffic = TrafficLight()
traffic.running()