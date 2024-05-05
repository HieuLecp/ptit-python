p= "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    nhap=input()
    if nhap[0]== '0':
        break
    k, s= nhap.split()
    k= int(k)
    res=""
    for i in s:
        res += p[(p.find(i)+k) % 28]
    print(res[::-1])

