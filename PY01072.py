n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
l = []
for i in a:
    if i not in l:
        l.append(i)
l.sort()
n = len(l)
b = []
def Try(idx):
    if len(b) == k:
        for i in b:
            print(i, end = ' ')
        print()
        return
    if idx == n:
        return
    for i in range(idx, len(l)):
        b.append(l[i])
        Try(i + 1)
        b.pop()
Try(0)