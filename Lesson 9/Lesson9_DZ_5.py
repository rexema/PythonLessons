class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f'Ничанию рисовать ручкой')


class Pencile(Stationery):
    def draw(self):
        print(f'Делаю карандашный набросок')


class Handle(Stationery):
    def draw(self):
        print(f'Делаю рисунок маркерами')


pen = Pen("Ручка")
pen.draw()
pencil = Pencile("Карандаш")
pencil.draw()
handle=Handle("Маркер")
handle.draw()
