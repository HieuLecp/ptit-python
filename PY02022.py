from math import sqrt
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
n= int(input())
a= list(map(int, input().split()))
b=set()
for i in a:
    if i not in b:
        if snt(i):
            print(i, a.count(i))
        b.add(i)


