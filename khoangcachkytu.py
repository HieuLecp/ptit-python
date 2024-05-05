t= int(input())
while t>0:
    s1= input()
    s2=s1[::-1]
    check=True
    for i in range(1, len(s1)):
        if abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1])):
            check=False
    if check:
        print("YES")
    else:
        print("NO")
    t -= 1