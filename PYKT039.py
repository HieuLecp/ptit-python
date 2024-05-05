for _ in range(int(input())):
    n= int(input())
    a=list(map(int, input().split()))
    b= list(map(int, input().split()))
    a.sort(), b.sort()
    def check(n):
        for i in range(n):
            if a[i] > b[i]:
                return "NO"
        return "YES"
    print(check(n))