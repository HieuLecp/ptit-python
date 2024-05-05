for _ in range(int(input())):
    n, m= map(int, input().split())
    a=list(map(int, input().split()))
    Max=0
    for i in range(n):
        if a[i] > a[Max]:
            Max=i
    a.insert(Max,m)
    for i in a:
        if i < 0:
            print(i, end=' ')
    for i in a:
        if i >=0:
            print(i, end=' ')
    print()