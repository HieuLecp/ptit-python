f=[0,1,1]
for i in range(3,93):
    f.append(f[i-1] + f[i-2])
for _ in range(int(input())):
    a, b= map(int,input().split())
    for j in range(a,b+1):
        print(f[j], end=" ")
    print()