class SinhVien:
    def __init__(self, hoten, sobailamdung, solansubmit):
        self.hoten = hoten
        self.sobailamdung = sobailamdung
        self.solansubmit = solansubmit
        
a= []

for _ in range(int(input())):
    x= input()
    y, z= map(int, input().split())
    a.append(SinhVien(x, y, z))
a.sort(key= lambda i : ((-1) * i.sobailamdung, i.solansubmit, i.hoten))
for i in a:
    print('{} {} {}'.format(i.hoten, i.sobailamdung, i.solansubmit))