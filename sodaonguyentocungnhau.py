import math
t= int(input())
while t>0:
    n= input()
    m=n[::-1]
    a= int(n)
    b=int(m)
    if math.gcd(a,b) == 1:
        print("YES")
    else:
        print("NO")
    t -= 1