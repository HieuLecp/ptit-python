n, m = map(int, input().split())
a = list()
for i in range(n):
    x = list(map(int, input().split()))
    a.append(x)
Min, Max = 999999, 0
for i in range(n):
    for j in range(m):
        Min = min(Min, a[i][j])
        Max = max(Max, a[i][j])
k = Max - Min
found = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == k:
            found = 1
if found > 0:
    print(k)
    for i in range(n):
        for j in range(m):
            if a[i][j] == k:
                print('Vi tri [{}][{}]'.format(i, j))
else:
    print('NOT FOUND')