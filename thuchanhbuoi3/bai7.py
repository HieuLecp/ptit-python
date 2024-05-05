n, q = map(int, input().split())
l = [0] * (n + 1)
for i in range(q):
    x, y = map(int, input().split())
    l[x - 1] += 1
    l[y] -= 1
for i in range(1, n):
    l[i] += l[i - 1]
for i in range(n):
    print(l[i] % 2, end=' ')