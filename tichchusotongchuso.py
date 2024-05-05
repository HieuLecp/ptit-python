t= int(input())
while t>0:
    s= input()
    tong=0
    tich=1
    for i in range(0, len(s)):
        if i%2 == 1:
            tong += int(s[i])
        elif i%2 == 0:
            if s[i] != '0':
                tich *= int(s[i])
    print(tich, end=" ")
    print(tong)
    t -= 1