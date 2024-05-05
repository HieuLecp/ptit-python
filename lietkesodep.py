t= int(input())

def check(s):
    if s != s[::-1]:
        return False
    if len(s)%2 != 0:
        return False
    for i in s:
        if int(i) % 2==1:
            return False
    return True

while t>0:
    n=input()
    i=22
    while i<int(n):
        if check(str(i)):
            print(i, end=" ")
        i += 2
    print()
    t -= 1