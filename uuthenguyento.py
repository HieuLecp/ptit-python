from math import sqrt
t= int(input())

def snt(n):
    if n==2 or n==3:
        return True
    elif n<2 or n%2 == 0 or n%3 == 0:
        return False
    i=5
    while i<=sqrt(n):
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True

def check(s):
    if snt(len(s)) == False:
        return "NO"
    dem1=dem2=0
    for i in s:
        if snt(int(i)):
            dem1 += 1
        else:
            dem2 += 1
    if dem2 > dem1:
        return "NO"
    return "YES"

while t>0:
    s= input()
    print(check(s))
    t -= 1