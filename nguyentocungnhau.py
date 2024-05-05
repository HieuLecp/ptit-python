import math

List= list(map(int, input().split()))
n, k= List
a=1
b=10
while k>1:
    a *=10
    b *= 10
    k -= 1
dem=0
for i in range(a, b):
    if math.gcd(i,n) == 1:
        print(i, end= " ")
        dem += 1
        if dem%10 == 0:
            print()
    
