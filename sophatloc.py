t= int(input())
while t>0:
    s= input()
    n=len(s)
    res= ""
    for i in range(n-2, n):
        res += s[i]
    if int(res) == 86:
        print("YES")
    else:
        print("NO")
    t -= 1