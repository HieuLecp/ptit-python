for _ in range(int(input())):
    x=input()
    # x += '*'
    res= 10 ** 19
    s=0
    for i in range(len(x)):
        if x[i].isdigit():
            s= s * 10 + int(x[i])
            if x[i+1].isalpha():
                res= min(res, s)
                s=0
    print(res)