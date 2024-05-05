from math import sqrt
# for _ in range(int(input())):
#     x= list(map(int, input().split()))
#     y= list(map(int, input().split()))
#     d=0
#     tich=0
#     for i in range(len(x)):
#         d += abs(x[i]-y[i]) ** 2
#         tich += x[i]*y[i]
#     d= format(sqrt(d), '.2f')
#     print(d, tich)

# IRIS1:
# import csv
# data=[]
# with open('/Users/leduchieu/Documents/Workspace/PTIT/python/iris.csv') as f:
#     f1= csv.reader(f)
#     data= [i for i in f1]
# for _ in range(int(input())):
#     tong=[]
#     a= input().split()
#     for x in data[1:]:
#         if a[0] == x[4] and a[1] == x[2]:
#             tong += [float(x[0])]
#     if len(tong) == 0:
#         print('INVALID')
#     else:
#         kq= format(sum(tong) / len(tong), '.4f')
#         print(kq)

# Flight 3:
# import json
# f= open('/Users/leduchieu/Documents/Workspace/PTIT/python/flights.json')
# b= json.load(f)
# for _ in range(int(input())):
#     a= input().split()
#     tong= 0
#     for i in b['flights']:
#         if int(i['year']) >= int(a[0]) and int(i['year']) < int(a[1]):
#             tong += int(i['passagers'])
#     if tong == 0:
#         print('INVALID')
#     else:
#         print(tong)

# Flight Year Month:
# import json
# f= open('/Users/leduchieu/Documents/Workspace/PTIT/python/flights.json')
# b= json.load(f)
# for _ in range(int(input())):
#     a= input().split()
#     tong=0
#     for x in b['flights']:
#         if int(a[0]) == int(x['year']) and a[1] == x['month']:
#             tong += int(x['passagers'])
#     if tong == 0:
#         print('INVALID')
#     else:
#         print(tong)


# IRIS 2:
# import csv
# data= []
# with open('/Users/leduchieu/Documents/Workspace/PTIT/python/iris.csv') as f:
#     f1= csv.reader(f)
#     data= [ row for row in f1]
# for _ in range(int(input())):
#     a= input().split()
#     ds=[]
#     for x in data[1:]:
#         if a[0] == x[4] and a[1] == 'sepal_length':
#             ds += [float(x[0])]
#         elif a[0] == x[4] and a[1] == 'sepal_width':
#             ds += [float(x[1])]
#         elif a[0] == x[4] and a[1] == 'petal_length':
#             ds += [float(x[2])]
#         elif a[0] == x[4] and a[1] == 'petal_width':
#             ds += [float(x[3])]
#     if len(ds) == 0:
#         print('INVALID')
#     elif a[2] == 'min':
#         print(format(min(ds), '.2f'))
#     elif a[2] == 'max':
#         print(format(max(ds), '.2f'))
#     elif a[2] == 'sum':
#         print(format(sum(ds), '.2f'))
#     elif a[2] == 'avg':
#         print(format(sum(ds) / len(ds), '.2f'))

