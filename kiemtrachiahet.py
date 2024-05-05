def kq(L, R, N):
    dem=0
    for i in range(L, R+1):
        check= False
        for j in range(2, N+1):
            if i%j == 0:
                check = True
                break
        if not check:
            dem += 1
    return dem               
while True:
    s = [x for x in input().split()]
    if(s[0] == "-1"):
        break
    l = s[0]
    r = s[1]
    # l,r= list(map(int, input().split()))
    # print(s[1])
    n=int(input())
    # if l==-1:break
    print(kq(int(l),int(r),n))
    