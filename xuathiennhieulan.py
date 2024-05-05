for _ in range(int(input())):
    n= int(input())
    a=list(map(int, input().split()))
    b= set(a)
    c=[]
    Max=1
    cmp=1
    for i in b:
        x=a.count(i)
        if x > n/2:
            c.append(x)
    print(c)
        