MOD = 10**9 + 7  # Khai báo modulo

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def count_pairs(test_cases):
    results = []
    for a, b in test_cases:
        result = 1
        for i in range(a, b + 1):
            result = (result * i) % MOD  # Tính tích của các số từ a đến b và lấy phần dư theo modulo
        results.append(result)
    return results

if __name__ == "__main__":
    t = int(input("Nhap so bo test: "))  # Nhập số bộ test
    test_cases = []
    for _ in range(t):
        a, b = map(int, input().split())  # Nhập giá trị của a và b cho mỗi bộ test
        test_cases.append((a, b))

    results = count_pairs(test_cases)

    for result in results:
        print(result)  # In kết quả cho mỗi bộ test
