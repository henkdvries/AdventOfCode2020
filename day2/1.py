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
    cc = tup[1].count(let)

    if(cc >= mi and cc <= ma):
        count += 1
for item in passw:
    checkpass(item)

print(count)


