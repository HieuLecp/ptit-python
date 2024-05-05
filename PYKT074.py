for _ in range(int(input())):
    a=input().split()
    b= a[0]
    for i in a[1:]:
        if (len(b) + len(i) + 1) > 100:
            break
        b += ' ' + i
    print(b)
    