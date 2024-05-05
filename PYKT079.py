for _ in range(int(input())):
    n= int(input())
    a=list(set(map(int, input().split())))
    a.sort()
    ans= a[-1] - a[0] - len(a) +1
    print(ans)