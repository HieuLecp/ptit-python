class NhanVien:
    def __init__(self, ma, ten, lcb, soCong):
        self.ma, self.ten, self.lcb, self.soCong = ma, ten, lcb, soCong

    def getPhongBan(self):
        return d.get(self.ma[3:])

    def calc(self):
        type = self.ma[0]
        soNam = int(self.ma[1:3])
        if type == 'A':
            if soNam <= 3:
                return 1000 * self.soCong * self.lcb * 10
            elif soNam <= 8:
                return 1000 * self.soCong * self.lcb * 12
            elif soNam <= 15:
                return 1000 * self.soCong * self.lcb * 14
            else:
                return 1000 * self.soCong * self.lcb * 20
        elif type == 'B':
            if soNam <= 3:
                return 1000 * self.soCong * self.lcb * 10
            elif soNam <= 8:
                return 1000 * self.soCong * self.lcb * 11
            elif soNam <= 15:
                return 1000 * self.soCong * self.lcb * 13
            else:
                return 1000 * self.soCong * self.lcb * 16
        elif type == 'C':
            if soNam <= 3:
                return 1000 * self.soCong * self.lcb * 9
            elif soNam <= 8:
                return 1000 * self.soCong * self.lcb * 10
            elif soNam <= 15:
                return 1000 * self.soCong * self.lcb * 12
            else:
                return 1000 * self.soCong * self.lcb * 14           
        else:
            if soNam <= 3:
                return 1000 * self.soCong * self.lcb * 8
            elif soNam <= 8:
                return 1000 * self.soCong * self.lcb * 9
            elif soNam <= 15:
                return 1000 * self.soCong * self.lcb * 11
            else:
                return 1000 * self.soCong * self.lcb * 13

    def __str__(self):
        return '{} {} {} {}'.format(self.ma, self.ten, self.getPhongBan(), self.calc())
    
d = dict()
for i in range(int(input())):
    x = input()
    p = 0
    for i in range(len(x)):
        if (x[i] == ' '):
            p = i
            break
    d[x[0:p]] = x[p + 1:]
for i in range(int(input())):
    print(NhanVien(input(), input(), int(input()), int(input())))