t= int(input())
while t>0:
    n= int(input())
    s=0
    if n%2 == 0:
        for i in range(2, n+1, 2):
            s += float(1/i)
    if n%2 ==1:
        for i in range(1, n+1, 2):
            s += float(1/i)
    s= "{:.6f}".format(s)
    print(s)
    t -= 1
            