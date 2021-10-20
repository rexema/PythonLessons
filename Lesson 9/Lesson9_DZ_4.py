class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.color} {self.name} поехала')

    def stop(self):
        print(f'Машина {self.color} {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.color} {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость вашей машины - {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости!')
        else:
            print(f'Скорость вашей машины - {self.speed} км/ч')


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости!')
        else:
            print(f'Скорость вашей машины - {self.speed} км/ч')


my_car = TownCar(50, "красный", "Ford", False)
my_car.go()
my_car.stop()
my_car.turn("направо")
my_car.show_speed()
my_car2 = WorkCar(120, "синяя", "Mazda", False)
my_car2.show_speed()
