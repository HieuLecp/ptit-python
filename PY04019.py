class NV:
    def __init__(self, i, name, lt, th):
        self.id= f'TS0{str(i)}'
        self.name= name
        self.diem= ((lt if lt<=10 else lt/10) + (th if th<=10 else th/10)) / 2
        if self.diem > 9.5:
            self.kq= "XUAT SAC"
        elif self.diem >= 8:
            self.kq= "DAT"
        elif self.diem >= 5:
            self.kq= "CAN NHAC"
        else:
            self.kq= "TRUOT"
    def __str__(self):
        return self.id + " " + self.name + " " + f'{round(self.diem, 2):.2f}' + " " + self.kq

a=[]
for t in range(int(input())):
    a.append(NV(t+1, input(), float(input()), float(input())))
a.sort(key= lambda x: (-x.diem))
for i in a:
    print(i)