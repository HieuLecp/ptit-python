from math import sqrt
t= int(input())

def check(s):
    sum=0
    for i in s:
        sum += int(i)
    if sum == 2 or sum == 3:
        return "YES"
    elif sum < 2 or sum%2 == 0 or sum%3 == 0:
        return "NO"
    i=5
    while i <= sqrt(sum):
        if sum%i == 0 or sum%(i+2) == 0:
            return "NO"
        i += 6
    return "YES"

while t>0:
    s= input()
    print(check(s))
    t -= 1