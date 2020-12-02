import re
with open('data.txt', 'r') as reader:
    passw = reader.readlines()


passw = { tuple(x.strip() for x in line.split(':')) for line in passw}

count = 0 



def checkpass(tup):
    global count
    mima, let = tup[0].split(' ')
    mi, ma = mima.split('-')
    mi = int(mi)
    ma = int(ma)
    
    if((tup[1][mi-1] == let) != (tup[1][ma-1] == let)):
        count += 1
for item in passw:
    checkpass(item)

print(count)