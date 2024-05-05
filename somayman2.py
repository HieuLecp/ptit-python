t= int(input())
while t>0:
    n=input()
    cnt=0
    for i in n:
        if i != '4' and i != '7':
            cnt += 1
    if cnt==0:
        print("YES")
    else:
        print("NO")
    t -= 1      