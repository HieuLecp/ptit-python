
n = int(input())
mon_hoc = []
for i in range(n):
    ma_mon = input().strip()
    ten_mon = input().strip()
    hinh_thuc_thi = input().strip()
    mon_hoc.append((ma_mon, ten_mon, hinh_thuc_thi))
mon_hoc.sort()
for mon in mon_hoc:
    print(mon[0], end=" ")
    print(mon[1], end=" ")
    print(mon[2])
