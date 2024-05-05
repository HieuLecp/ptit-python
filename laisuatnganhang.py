def laisuat(n, x, m):
    dem=0
    while n<m:
        n += n*(x/100)
        dem += 1
    return dem

t= int(input())
while(t>0):
    n, x, m = list(map(float, input().split()))
    sonam=laisuat(n, x, m)
    print(sonam)
    t -= 1
    