def tang(n):
    for i in range(1,len(n)):
        if n[i] == n[i-1]:
            return -1
        if n[i] < n[i-1]:
            return i
    return -1

def solve(n):
    if len(n) < 3:
        return "NO"
    a=tang(n)
    for i in range(a+1, len(n)):
        if n[i] > n[i-1]:
            return "NO"
    return "YES"

for _ in range(int(input())):
    n= input()
    print(solve(n))
    