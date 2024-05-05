n= input()
n= n[::-1]
res= n[0]
for i in range(1, len(n)):
    if (i)%3==0:
        res += ","
    res += n[i]
print(res[::-1])