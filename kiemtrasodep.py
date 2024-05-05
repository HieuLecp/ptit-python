t= int(input())

def check(n):
    if n[0] == n[1]:
        return "NO"
    for i in range(2, len(n)):
        if n[i] != n[i&1]:
            return "NO"
    return "YES"

while t>0:
    n= input()
    print(check(n))
    t -= 1