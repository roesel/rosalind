# http://rosalind.info/problems/orf/
# importing data
dataset = open('C:/Users/roese/Downloads/rosalind_long.txt').read().strip().split()

for i in range(len(dataset)):
    if dataset[i][0] == ">":
        dataset[i] = "-"

del dataset[0]
ds = ''.join(dataset)
d = ds.split('-')

import numpy as np

def ovrlp(a, b):
    o = ""
    for i in range(int(len(a)/2)):
        if i+len(b) < len(a):
            if a[i:i+len(b)] == b:
                o = a[i:i+len(b)]
                break
        else:
            if a[i:len(a)] == b[0:len(a[i:len(a)])]:
                o = a[i:len(a)]
                break
    if not (len(o)>len(a)/2 and len(o)>len(b)/2):
        o = ""
    return o

def m(d):
    e = np.zeros((len(d), len(d)), dtype=np.int)
    o = []
    for i in range(len(d)):
        for j in range(len(d)):
            if i != j:
                ov = ovrlp(d[i], d[j])
                e[i][j] = len(ov)
    return e

def house(m):
    di = {}
    for i in range(len(m[0])):
        a = np.argmax(m[i])
        if np.average(m[i]) != 0:
            #print(i, ' -> ', a)
            di[a] = i
        else:
            #print(i, ' -> ', a)
            di[len(m[0])] = i
    return di

def love(di):
    i = len(di)
    o = []
    while len(o)<len(di):
        o.append(di[i])
        i = di[i]
    return o[::-1]

def merge(l):
    nol = []
    for i in range(1, len(l)):
        nol.append(len(ovrlp(l[i-1], l[i])))
    out = l[0]
    for i in range(len(nol)):
        out = out + l[i+1][nol[i]:]
    return out


o = love(house(m(d)))  # unprofessional, but I'm epically annoyed
ds = []
for i in o:
    ds.append(d[i])
print(merge(ds))
