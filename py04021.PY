from datetime import datetime

class khach:
    def __init__(self, id, name, t1, t2):
        self.id= id
        self.name= name
        self.time= datetime.strptime(t2, '%H:%M') - datetime.strptime(t1, '%H:%M')

a=[]
for _ in range(int(input())):
   a.append(khach(input(), input(), input(), input()))
a.sort(key= lambda x: (-x.time)) 
for i in a:
    print(i.id, i.name, i.time.seconds//3600, 'gio', i.time.seconds//60%60, 'phut')