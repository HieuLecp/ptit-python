import math

s= input()
while len(s) % 3 >0:
    s = '0' + s
res=''
cnt=''
for i in range(0,len(s)):
    res += s[i]
    if len(res)==3:
        cnt += str(int(res,2))
        res=''
print(cnt)
