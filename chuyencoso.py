def chuyendoi(N,b):
    if N == 0:
        return '0'
    n= N
    dodai=0
    while n>0:
        n //=b
        dodai += 1
    kq=['0'] * dodai
    n=N
    for i in range(dodai-1, -1, -1):
        du= n % b
        if du<10:
            kq[i]= str(du)
        else:
            kq[i]= chr(ord('A') + du - 10)  
        n //= b  
    return ''.join(kq)

t= int(input())
while t>0:
    List= list(map(int, input().split()))
    N, b= List
    kq=chuyendoi(N,b)
    print(kq)
    t -= 1