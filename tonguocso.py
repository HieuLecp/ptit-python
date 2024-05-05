import math
a=[0]
for _ in range(int(input())):
    n=int(input())
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            while n%i==0:
                a.append(i)
                n/=i
    if n!=1 : a.append(n)
print(int(sum(a)))