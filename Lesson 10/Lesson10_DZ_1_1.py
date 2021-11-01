class Matrix:
    def __init__(self, input_data):
        self.input_data = input_data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input_data])

    def __add__(self, other):
        answer = ''
        if len(self.input_data) == len(other.input_data):
            for line_1, line_2 in zip(self.input_data, other.input_data):
                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join(map(str, summed_line)) + '\n'
        else:
            return f'Problems with shape'
        return answer


matrix = Matrix([[12, 22], [34, 34], [54, 67]])
matrix2 = Matrix([[34, 45], [45, 34], [44, 78]])
print(matrix)
print(matrix + matrix2)
# print(matrix)
