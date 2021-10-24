class Cell:
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return self.param + other.param

    def __sub__(self, other):
        if self.param - other.param > 0:
            return self.param - other.param
        else:
            raise ValueError(f'Negative result')

    def __mul__(self, other):
        return self.param * other.param

    def __truediv__(self, other):
        return self.param / other.param

    def make_order(self, n_cells):
        rows = round(self.param / n_cells)
        row_left = self.param % n_cells
        cell = "*" * n_cells
        cell_left = "*" * row_left
        if self.param % n_cells == 0:
            return f'\n{cell}' * rows
        else:
            return f'\n{cell}' * rows + f'\n {cell_left}'


cell1 = Cell(30)
cell2 = Cell(15)
print(cell1 + cell2)
print(cell1/cell2)
print(cell1.make_order(10))
print(cell2.make_order(2))
