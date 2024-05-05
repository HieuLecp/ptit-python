t= int(input())

def check(s):
    if len(s)%2 == 0 or s[0] == s[1]:
        return "NO"
    kt= s[0]
    for i in range(2, len(s), 2):
        if s[i] != kt:
            return "NO"
        kt= s[i]
    return "YES"

while t>0:
    s= input()
    print(check(s))
    t -= 1