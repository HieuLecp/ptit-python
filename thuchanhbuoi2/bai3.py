MOD = 10**9 + 7
def count_ways(M, N):
    if M == 0 or N == 0:
        return 1
    return (2 ** (M * N)) % MOD
T = int(input())
for _ in range(T):
    M, N = map(int, input().split())
    result = count_ways(M, N)
    print(result)
