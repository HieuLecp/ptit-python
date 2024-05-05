t=int(input())
while t>0:
    a= input()
    dem=1
    for i in range(1, len(a)):
        if a[i-1] != a[i]:
            print(dem, end= "")
            print(a[i-1], end= "")
            dem=1
        else:
            dem += 1
    print(dem, end= "")
    print(a[len(a)-1])
    t -= 1