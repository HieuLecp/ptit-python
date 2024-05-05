t= int(input())

def check(n):
    if int(n) != int(n[::-1]):
        return False
    for i in n:
        if int(i) % 2 != 0:
            return False
    if int(len(n)) % 2 != 0:
        return False
    return True

while t>0:
    n= input()
    i=22
    while i<int(n):
        if check(str(i)):
            print(i, end= " ")
        i += 2
    print()
    t -= 1