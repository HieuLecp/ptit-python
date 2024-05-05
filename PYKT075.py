from datetime import datetime
file= open('/Users/leduchieu/Documents/Workspace/PTIT/python/SOTAY.txt', 'r')

s= file.read()
a=[]

for i in s.split('\n'):
    if len(i) > 0:
        a.append(i)
        
class person:
    def __init__(self, d, m, y, hoten, sdt):
        self.d= d
        self.m= m
        self.y= y
        self.hoten= hoten
        x= hoten.split()
        self.ten= x[-1]
        self.hodem= ''
        for i in range(len(x) - 1):
            self.hodem += x[i] + ' '
        self.sdt= sdt
    def toString(self):
        return '{}: {} {}/{}/{}'.format(self.hoten, self.sdt, self.d, self.m, self.y)
L= []
id=0
datetime= ''
while id <len(a):
    if '/' in a[id]:
        datetime= a[id].split()[1]
        id += 1
    else:
        d, m, y= map(int, datetime.split('/'))
        L.append(person(d, m, y, a[id], a[id+1]))
        id += 2
def cmp(a):
    return (a.ten, a.hodem)

L.sort(key=cmp)
for i in L:
    print(i.toString())