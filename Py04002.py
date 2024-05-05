
class Rectangle:
    def __init__(self, cd, cr, mau):
        self.cd= cd
        self.cr= cr
        self.mau= mau
    def perimeter(self):
        return (self.cd + self.cr) * 2
    def area(self):
        return self.cd * self.cr
    def color(self):
        return self.mau[0].upper() + self.mau[1:].lower()
arr= input().split()
if int(arr[0]) > 0 and int(arr[1]) > 0:
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print('INVALID')
        