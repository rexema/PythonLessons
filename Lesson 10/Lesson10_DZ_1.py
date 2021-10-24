class Matrix:
    def __init__(self, *args):
        self.list = []
        for el in args:
            self.list.append(el)

    def __str__(self):

        for el in self.list:
            if len(el) == 3:

                return f'{self.list[0][0]}  {self.list[0][1]}  {self.list[0][2]}\n{self.list[1][0]}  {self.list[1][1]}  {self.list[1][2]}\n{self.list[2][0]}  {self.list[2][1]}  {self.list[2][2]}'
            elif len(el) == 2:
                return f'{self.list[0][0]}  {self.list[0][1]}\n{self.list[1][0]}  {self.list[1][1]}\n{self.list[2][0]}  {self.list[2][1]}'
            else:
                return f'{self.list[0][0]}  {self.list[0][1]}  {self.list[0][2]}  {self.list[0][3]}\n{self.list[1][0]}  {self.list[1][1]}  {self.list[1][2]}  {self.list[1][3]}'


matrix = Matrix([34, 45], [67, 78], [23, 12])
print(matrix)
