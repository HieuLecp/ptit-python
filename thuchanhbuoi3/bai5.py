class SinhVien:
    def __init__(self, ma, ten, lop):
        self.ma, self.ten, self.lop, self.cc, self.note = ma, ten, lop, 10, ''

    def calc(self, dd):       
        for i in dd:
            if i == 'v':
                self.cc -= 2
            elif i == 'm':
                self.cc -= 1
        if self.cc <= 0:
            self.cc = 0
            self.note = ' KDDK'

    def __str__(self):
        return '{} {} {} {}{}'.format(self.ma, self.ten, self.lop, self.cc, self.note)

sv = list()
d = dict()
n = int(input())
for i in range(n):
    sv.append(SinhVien(input(), input(), input()))
for i in sv:
    d[i.ma] = i
for i in range(n):
    x = input().split()
    d[x[0]].calc(x[1])
for i in sv:
    print(i)