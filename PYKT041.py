def count_coin_pairs(grid):
    n = len(grid)
    rows = [0] * n
    columns = [0] * n
    total_pairs = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'C':
                rows[i] += 1
                columns[j] += 1

    for count in rows:
        total_pairs += count * (count - 1) // 2

    for count in columns:
        total_pairs += count * (count - 1) // 2

    return total_pairs

n= int(input())
a=[]
for i in range(n):
    a.append(input())
kq= count_coin_pairs(a)
print(kq)
