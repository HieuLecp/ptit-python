n= int(input())
a=[]
for i in range(n):
    a.append(input())
def kq(s1, s2):
    if s1 == s2:
        return 0
    for i in range(len(s1)):
        s2= s2[1:] + s2[0]
        if s2 == s1:
            return i+1
    return -1
ans= 10**5
check= True
for i in range(n):
    cnt= 0
    for j in range(n):
        if i != j:
            num= kq(a[i], a[j])
            if num == -1:
                check= False
                break
            else:
                cnt += num
    ans = min(ans, cnt)
if check:
    print(ans)
else:
    print("-1")  
        