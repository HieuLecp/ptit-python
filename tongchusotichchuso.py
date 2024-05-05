t= int(input())
while t>0:
    s= input()
    tong=0
    tich=1
    for i in range(0, len(s)):
        if i%2 == 0:
            tong += int(s[i])
        elif i%2 == 1:
            if s[i] != '0':
                tich *= int(s[i])
    if tich == 1:
        tich=0
    print(tong, end=" ")
    print(tich)
    t -= 1