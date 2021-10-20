
class Road:
    def __init__(self, length, width, thickness):
        self.length = length
        self.width = width
        self.thickness = thickness

    def mass(self):
        mass = round((self.length * self.width * 25 * self.thickness) / 1000)
        print(
            f'Масса асфальта для покрытия 1 кв.метра дороги асфальтом толщиной в {self.thickness}см.равняется {mass}т.')


road = Road(20, 5000, 5)
road.mass()
