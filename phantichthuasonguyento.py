import math
t= int(input())
while t>0:
    n=int(input())
    m= int(math.sqrt(n))
    print("1", end= "")
    for i in range(2, m+1):
        if n%i==0:
            print(" * ",end= "")
            dem=0
            while n%i==0:
                dem += 1
                n //= i
            print(str(i) + "^" + str(dem), end= "")
            m=int(math.sqrt(n))
    if n>1:
        print(" * " + str(n) + "^" + str(1), end= "")
    print()
    t -= 1       
    