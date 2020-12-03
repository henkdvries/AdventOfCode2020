import numpy as np
import itertools as it
with open('data.txt', 'r') as reader:
    output = reader.readlines()

routemap = [[x for x in line.rstrip()] for line in output]

steplist = {(1,1), (3,1), (5,1), (7,1), (1,2)}
val = []

def route(x, y):
    stepscount = 0
    treecount = 0
    for cnt,line in enumerate(routemap): 
        if(cnt%y==0):
            if(line[((x*stepscount) % len(line))] == '#'):
                treecount += 1
            stepscount += 1
    return treecount

for step in steplist:
    val.append(route(step[0], step[1]))
print(val)
x = np.array(val)
x = x.astype(np.int64)
print(np.prod(x))