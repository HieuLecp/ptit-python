from math import sqrt
def check(n):
    if n==2 or n==3:
        return True
    if n<2 or n%2 == 0 or n%3 == 0:
        return False
    i=5
    while i<sqrt(n)+1:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i += 6
    return True

snt=[2]
for i in range(3,8000,2):
    if check(i):
        snt.append(i)
N, X=list(map(int, input().split()))
print(X, end=" ")
for i in range(N):
    print(X+snt[i], end=" ")
    X += snt[i]