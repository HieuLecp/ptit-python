def check(a, b):
    a.sort()
    b.sort()
    for i in range(len(a)):
        if (a[i] > b[i]):
            return False
    return True

for test in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if check(a, b):
        print('YES')
    else:
        print('NO')