from math import sqrt
t= int(input())

def check(n):
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

def kq(s):
    for i in range(0, len(s)):
        if check(i) == True and check(int(s[i])) == False:
            return "NO"
        elif check(i) == False and check(int(s[i])) == True:
            return "NO"
    return "YES"

while t>0:
    s= input()
    print(kq(s))
    t -= 1