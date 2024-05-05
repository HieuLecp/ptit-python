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

while t>0:
    s= input()
    res=""
    for i in range(len(s)-4, len(s)):
        res += s[i]
    if check(int(res)):
        print("YES")
    else:
        print("NO")
    t -= 1