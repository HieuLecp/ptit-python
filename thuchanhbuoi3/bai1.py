class Matrix:
    def __init__(self, n, m, a):
        self.n, self.m, self.a = n, m, a

    def rev(self):
        b = list()
        for i in range(self.m):
            x = list()
            for j in range(self.n):
                x.append(self.a[j][i])
            b.append(x)
        return b
    
    def mul(self):
        c = list()
        b = self.rev()
        for i in range(self.n):
            x = list()
            for j in range(self.n):
                tmp = 0
                for k in range(self.m):
                    tmp += self.a[i][k] * b[k][j]
                x.append(tmp)
            c.append(x)
        return c
    
for test in range(int(input())):
    n, m = map(int, input().split())
    a = list()
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    x = Matrix(n, m, a)
    y = x.mul()
    # print(x.rev())
    for i in range(n):
        for j in range(n):
            print(y[i][j], end=" ")
        print()