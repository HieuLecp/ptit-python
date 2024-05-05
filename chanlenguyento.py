from math import sqrt
t= int(input())

def snt(n):
    if n==2 or n==3:
        return True
    if n<2 or n%2 == 0 or n%3 == 0:
        return False
    i=5
    while i<=sqrt(n):
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True

def check(s):
    sum =0
    for i in range(0, len(s)):
        if i%2 == 0 and int(s[i])%2 == 1:
            return "NO"
        elif i%2 == 1 and int(s[i])%2 == 0:
            return "NO"
        sum += int(s[i])
    if snt(sum) == False:
        return "NO"
    return "YES"

while t>0:
    s= input()
    print(check(s))
    t -= 1