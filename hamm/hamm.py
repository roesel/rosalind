from __future__ import division
import inspect
rid = inspect.getfile(inspect.currentframe()).replace('.py', '').split('/')[-1]

def get_params():
    strings = []
    with open('rosalind_'+rid+'.txt', 'r') as datafile:
        for line in datafile:
            strings.append(line.replace('\n', ''))
    return tuple(strings)

a, b = get_params()

n=0
u=zip(a,b)
for i,j in u:
    if (i!=j):
        n+=1
print n