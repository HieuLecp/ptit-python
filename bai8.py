MOD = 10**9 + 7
def binomial_coefficient(n, k):
    if k == 0 or k == n:
        return 1
    if k > n - k:
        k = n - k
    result = 1
    for i in range(k):
        result = (result * (n - i)) // (i + 1)
    return result
def find_difference_sum(N, K, A):
    A.sort()
    total_sum = 0
    for i in range(K - 1, N):
        total_sum = (total_sum + (A[i] - A[N - i - 1]) * binomial_coefficient(i, K - 1)) % MOD
    return total_sum
N, K = map(int, input().split())
A = list(map(int, input().split()))
result = find_difference_sum(N, K, A)
print(result)
