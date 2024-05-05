import math
t= int(input())

def gcd(a, b):
    while a != b:
        if a>b:
            a -= b
        else:
            b -= a
    return a

def check(n):
    if n==2 or n==3:
        return True
    elif n<2 or n%2==0 or n%3==0:
        return False
    i=2
    m= math.sqrt(n)
    while i<=m:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True

def tong(n):
    cnt=0
    while n!=0:
        cnt += int(n%10)
        n //= 10
    return cnt

while t>0:
    List= list(map(int, input().split()))
    a, b= List
    if check(tong(gcd(a,b))):
        print("YES")
    else:
        print("NO")
    t -= 1