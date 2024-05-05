dp = [0] * 100005
mod =  1000000007
def gt() :
    dp[0] = 1 
    dp[1] = 1 
    for i in range(2,100005) :
        dp[i] = dp[i-1] * i
        dp[i] %= mod
def poww(a,b) :
    if b == 0 : return 1 
    c = poww(a,b//2)
    if b  % 2 == 0 : return ((c % mod) * ( c % mod)) % mod
    return ((a % mod) * (((c % mod) * ( c % mod)) % mod))% mod
def calc(n,k) :
    tmp = dp[k] * dp[n-k]
    tmp%=mod
    return (dp[n] * poww(tmp,mod - 2))% mod
n , k = list(map(int, input().strip().split()))
a = [0] + list(map(int, input().strip().split()))
gt()
a.sort()
ans1 , ans2 = 0 , 0
if k == 1 : print(0)
else :
    for i in range(1,n+1) :
        if i+k-1 > n :break
        ans1+=a[i] * calc(n - i , k-1) 
        ans1%=mod
    for i in range(1, n+1) :
        if i -k +1 < 1 : continue
        ans2+=a[i] * calc(i-1 , k-1)
        ans2 %= mod
    ans = ans2 - ans1
    print((ans + mod * mod)%mod)