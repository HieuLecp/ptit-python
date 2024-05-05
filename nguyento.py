import math
from re import T

t= int(input())

def check(n) :
    if n==2 or n==3:
        return True
    if n<2 or n%2 == 0 or n%3 == 0:
        return False
    m=math.sqrt(n)
    i=5
    while i<=m:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True

while t>0 :
    n=int(input())
    dem=0
    for i in range(1, n) :
        if math.gcd(n, i) == 1 :
            dem += 1
    if check(dem) :
        print("YES")
    else :
        print("NO")
    t -= 1
            