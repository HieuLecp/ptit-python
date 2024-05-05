import datetime

class Bill:
    def __init__(self, id, name, phong, start, finish, add):
        self.id = 'KH{:02d}'.format(id)
        self.name = name
        self.phong, self.start, self.finish, self.add = phong, start, finish, add
        self.calc()
    
    def calc(self):
        d1, m1, y1 = map(int, self.start.split('/'))
        d2, m2, y2 = map(int, self.finish.split('/'))
        self.diff = datetime.date(y2, m2, d2) - datetime.date(y1, m1, d1)
        if self.phong[0] == '1':
            gia = 25
        if self.phong[0] == '2':
            gia = 34
        if self.phong[0] == '3':
            gia = 50
        if self.phong[0] == '4':
            gia = 80
        self.final = gia * (self.diff.days + 1) + self.add

    def __str__(self):
        return '{} {} {} {} {}'.format(self.id, self.name, self.phong, self.diff.days + 1, self.final)
    
l = list()
for i in range(int(input())):
    l.append(Bill(i + 1, input().strip(), input().strip(), input().strip(), input().strip(), int(input().strip())))
l.sort(key=lambda x:-x.final)
for i in l:
    print(i)