import math
t= int(input())

def check(s):
    n= len(s)
    cnt=int(s[0])
    for i in range(1, n):
        if(abs(int(s[i]) - int(s[i-1])) != 2):
            return False
        cnt += int(s[i])
    if cnt%10==0:
        return True

while t>0:
    s= input()
    if  check(s) == True:
        print("YES")
    else:
        print("NO")
    t -= 1
    