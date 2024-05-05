import math
class PhanSo:
    def __init__(self, tu, mau):
        self.tu= tu
        self.mau= mau
    def rutgon(self):
        GCD= math.gcd(self.tu, self.mau)
        self.tu //= GCD
        self.mau //= GCD
        return self
    def tong(self, o):
        mau= (self.mau * o.mau) // math.gcd(self.mau, o.mau)
        res = PhanSo(self.tu * mau // self.mau + o.tu * mau // o.mau, mau)
        return res.rutgon()
    
a, b, c, d= list(map(int, input().split()))
A= PhanSo(a, b)
B= PhanSo(c, d)
C= A.tong(B)
print(str(C.tu) + '/' + str(C.mau))