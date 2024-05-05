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
    s1=s2=""
    for i in range(0,3):
        s1 += s[i]
    for i in range(len(s)-3, len(s)):
        s2 += s[i]
    if snt(int(s1)) and snt(int(s2)):
        return "YES"
    return "NO"

while t>0:
    s= input()
    print(check(s))
    t -= 1