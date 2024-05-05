n= int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
k= int(input())
nuatren=0
nuaduoi=0
for i in range(n):
    for j in range(n):
        if j > n-i-1:
            nuaduoi += a[i][j]
        elif j < n-i-1:
            nuatren += a[i][j]
dochenhlech=abs(nuatren - nuaduoi)
if dochenhlech <= k:
    print("YES")
else:
    print("NO")
print(dochenhlech)
