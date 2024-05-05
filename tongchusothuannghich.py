t= int(input())

def check(s):
    sum=0
    for i in s:
        sum += int(i)
    sum= str(sum)
    if sum != sum[::-1] or len(sum) <= 1:
        return "NO"
    return "YES"

while t>0:
    s= input()
    print(check(s))
    t -= 1