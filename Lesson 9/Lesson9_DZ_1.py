import itertools
from itertools import cycle
import time


class TrafficLight:
    def __init__(self, color1, color2, color3):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3

    def running(self):
        colors = [self.color1, self.color2, self.color3]

        colors2 = cycle(colors)

        for color in itertools.cycle(colors2):
            print(color)
            time.sleep(7)
            print(next(colors2))
            time.sleep(4)
            print(next(colors2))
            time.sleep(5)


traffic_light = TrafficLight("красный", "жёлтый", "зелёный")
traffic_light.running()
