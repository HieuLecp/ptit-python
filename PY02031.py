from math import sqrt
def check(n):
    if n == 2 or n == 3:
        return 1
    elif n<2 or n%2 == 0 or n%3 == 0:
        return 0
    i=5
    while i<=sqrt(n):
        if n%i == 0 or n%(i+2) == 0:
            return 0
        i += 6
    return 1
n, m=map(int, input().split())
for i in range(n):
    a=list(map(int,input().split()))
    for j in a:
        print(check(j), end=' ')
    print()
