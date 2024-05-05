class ThiSinh:
    def __init__(self, hoten, ngaysinh, diem1, diem2, diem3):
        self.hoten= hoten
        self.ngaysinh= ngaysinh
        self.diem1= diem1
        self.diem2= diem2
        self.diem3= diem3
        self.tongdiem= diem1 + diem2 + diem3
    
    def output(self):
        return (f"{self.hoten} {self.ngaysinh} {self.tongdiem:.1f}")
    
ten=input()
ngaysinh=input()
diem1=float(input())
diem2=float(input())
diem3=float(input())
A= ThiSinh(ten, ngaysinh, diem1, diem2, diem3)
print(A.output())