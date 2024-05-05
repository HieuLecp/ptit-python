class Matrix:
    def __init__(self, n, m, elements):
        self.n = n
        self.m = m
        self.elements = elements

    def transpose(self):
        transposed_matrix = [[self.elements[j][i] for j in range(self.n)] for i in range(self.m)]
        return Matrix(self.m, self.n, transposed_matrix)

    def multiply(self, other):
        result_matrix = [[0 for _ in range(other.m)] for _ in range(self.n)]

        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    result_matrix[i][j] += self.elements[i][k] * other.elements[k][j]

        return Matrix(self.n, other.m, result_matrix)

    def display(self):
        for row in self.elements:
            print(*row)

for _ in range(int(input())):
    n, m= list(map(int, input().split()))
    elements = [list(map(int, input().split())) for _ in range(n)]
    matrix_a = Matrix(n, m, elements)
    transposed_matrix_a = matrix_a.transpose()
    result_matrix = matrix_a.multiply(transposed_matrix_a)
    result_matrix.display()