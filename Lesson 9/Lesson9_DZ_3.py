class Worker:
    def __init__(self, name, surname, position=None, _income=None):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


def get_total_income(wage, bonus):
    _income = {"оклад": wage, "премия": bonus}
    print(f'Доход с учётом премии составляет {int(wage) + int(bonus)}')
    print(_income)


class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)


me = Position("Анастасия", "Соснина")
me.get_full_name()
get_total_income(2000, 3000)
