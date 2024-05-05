from math import sqrt
t= int(input())

def check(n):
    if n == 2 or n == 3:
        return True
    elif n<2 or n%2 == 0 or n%3 == 0:
        return False
    i=5
    while i<=sqrt(n):
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True

def kq(s):
    if check(len(s)) == False:
        return "NO"
    n=0
    for i in s:
        if check(int(i)):
            n += 1
    m= int(len(s))-n
    if n<m:
        return "NO"
    return "YES"

while t>0:
    n= input()
    print(kq(n))
    t -= 1