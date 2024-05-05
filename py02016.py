for _ in range(int(input())):
    n= int(input())
    a= list(map(int, input().split()))
    mymap= {}
    Max=1
    num = int(1e7)
    for i in a:
        if i not in mymap:
            mymap[i] = 1
        else:
            mymap[i] += 1
    Max= max(mymap.values())
    for f, s in mymap.items():
        if s == Max:
            Max = s
            num = min(num, f)
    if(Max > n // 2):
        print(num)
    else:
        print("NO")