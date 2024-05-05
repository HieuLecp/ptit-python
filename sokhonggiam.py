t= int(input())
while t>0:
    a= input()
    check=True
    for i in range(0, len(a) -2, 1):
        if a[i] > a[i+1]:
            check=False
    if check == True:
        print("YES")
    else:
        print("NO")
    t -= 1
        
