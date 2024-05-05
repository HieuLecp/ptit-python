from math import sqrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, o):
        return sqrt((self.x - o.x) ** 2 + (self.y - o.y) ** 2)

class Triangle:
    def __init__(self, Point1, Point2, Point3):
        self.Point1= Point1
        self.Point2= Point2
        self.Point3= Point3
    def check(self):
        a = self.Point1.distance(self.Point2)
        b = self.Point2.distance(self.Point3) 
        c = self.Point1.distance(self.Point3)
        return a+b > c and b+c > a and a+c > b
    def dientich(self):
        a = self.Point1.distance(self.Point2)
        b = self.Point2.distance(self.Point3) 
        c = self.Point1.distance(self.Point3)
        if self.check():
            return "{:.2f}".format(sqrt((a+b+c) * (a+b-c) * (b+c-a) * (c+a-b))/4)
        else:
            return "INVALID"
a=[]
t= int(input())
for i in range(t):
    a += [float(j) for j in input().split()]
j=0
for index in range(t):
    triangle= Triangle(Point(a[j], a[j+1]), Point(a[j+2], a[j+3]), Point(a[j+4], a[j+5]))
    print(triangle.dientich())
    j += 6