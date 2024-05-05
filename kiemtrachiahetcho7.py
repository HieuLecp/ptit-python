t= int(input())

def kq(n):
    s=0
    if int(n)%7 == 0:
        return n
    for i in range(0,1000):
        s=int(n) + int(n[::-1])
        if s%7 == 0:
            return s
            break
        n= str(s)
    return -1

while t>0:
    n= input()
    print(kq(n))
    t -= 1
    