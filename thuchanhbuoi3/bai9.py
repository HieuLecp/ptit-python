class Bill:
    def __init__(self, id, name, type, lastNum, currentNum):
        self.id = 'KH{:02d}'.format(id)
        tmp = name.split()
        self.name = ''
        for i in tmp:
            self.name += i.capitalize() + " "
        self.name = self.name[0:len(self.name) - 1]
        self.type = type
        self.lastNum = lastNum
        self.currentNum = currentNum
        self.calculate()

    def calculate(self):
        cnt = self.currentNum - self.lastNum
        if self.type == 'A':
            range = 100
        if self.type == 'B':
            range = 500
        if self.type == 'C':
            range = 200
        if cnt <= range:
            self.calc1 = cnt * 450
            self.calc2 = 0
            self.vat = 0
            self.total = cnt * 450
        else:
            self.calc1 = range * 450
            self.calc2 = (cnt - range) * 1000
            self.vat = (cnt - range) * 1000 // 20
            self.total = self.calc1 + self.calc2 + self.vat
        

    def __str__(self):
        return '{} {} {} {} {} {}'.format(self.id, self.name, self.calc1, self.calc2, self.vat, self.total)


list = []
for i in range(int(input())):
    name = input().strip()
    x = input().strip().split()
    type, l, c = x[0], x[1], x[2]
    last = int(l)
    current = int(c)
    list.append(Bill(i + 1, name, type, last, current))

list.sort(key=lambda e: (-e.total))
print(*list, sep='\n')