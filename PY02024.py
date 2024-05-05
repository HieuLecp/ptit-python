def sum(n):
    n=str(n)
    s=1
    for i in n:
        s *= int(i)
    return s
def sapxep(n):
    return sorted(n,key=lambda x : (sum(x), x))
for _ in range(int(input())):
    n= int(input())
    a= list(map(int,input().split()))
    a= sapxep(a)
    for i in a:
        print(i, end=" ")
    print()
    