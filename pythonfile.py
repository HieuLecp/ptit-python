def check(s):
    n=len(s)
    if n<3:
        return False
    s= s.lower()
    if s[n-3:] != '.py':
        return False
    for i in s:
        if ord(i) < ord('a') and ord(i) > ord('z') and ord(i) != ord('.') and ord(i) != ord('_'):
            return False
    return True
    
s=input()
if check(s):
    print("yes")
else:
    print("no")