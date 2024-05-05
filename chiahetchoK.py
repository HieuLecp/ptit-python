List= list(map(int, input().split()))
b= []
a, k, n= List
i= k- a%k
n -= a
while i<=n:
    b.append(i)
    i += k
if len(b) == 0:
    print("-1")
for i in b:
    print(i, end = " ")