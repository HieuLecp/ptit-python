t= int(input())
while t>0:
    s= input()
    List= list()
    for i in range(0, len(s)-1, 2):
        dem= int(s[i+1])
        while dem > 0:
            List.append(s[i])
            dem -= 1
    for i in List:
        print(i, end = "")
    print()
    t -= 1
        