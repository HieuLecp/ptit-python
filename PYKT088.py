from math import sqrt
def dem(n):
    count=0
    i=1
    while i < sqrt(n):
        if count == 9:
            return 1
        if n%i == 0:
            count += 1
        n %= i
    if n > 1:
        count +=1
    if count == 9:
        return 1
    return 0
n= int(input())
