from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, o):
        return "{:.4f}".format(sqrt((self.x - o.x) ** 2 + (self.y - o.y) ** 2))

def Decimal(n):
    return float(n)

if __name__ == '__main__':
    t= int(input())
    while t > 0:
        arr= input().split()
        p1= Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1