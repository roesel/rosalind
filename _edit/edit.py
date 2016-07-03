# http://rosalind.info/problems/edit/
from itertools import combinations

# importing data
dataset = open('C:/Users/roese/Downloads/rosalind_edit_.txt').read().strip().split()

for i in range(len(dataset)):
    if dataset[i][0] == ">":
        dataset[i] = "-"

del dataset[0]
ds = ''.join(dataset)
dataset = ds.split('-')

a = dataset[0]
b = dataset[1]

import numpy as np

def find_M(a, b):
    ''' returns the M matrix as per https://en.wikipedia.org/wiki/Longest_common_subsequence_problem '''
    # find values of M.
    M = np.zeros((len(a)+1,len(b)+1))
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                M[i+1][j+1] = M[i][j]+1
            else:
                M[i+1][j+1] = max(M[i+1][j],M[i][j+1])
    return M

def lcsq(a, b):
    M = find_M(a, b)
    # Recover a maximum substring.
    longest_sseq = ''
    numsi = []
    numsj = []
    i,j = len(a), len(b)
    while i*j != 0:
        if M[i][j] == M[i-1][j]:
            i -= 1
        elif M[i][j] == M[i][j-1]:
            j -= 1
        else:
            longest_sseq = a[i-1] + longest_sseq
            numsi.insert(0, i-1)
            numsj.insert(0, j-1)
            i -= 1
            j -= 1

    return longest_sseq, numsi, numsj


lc = "pes"
while lc:
    print(len(a)-len(b))
    lc, na, nb = lcsq(a, b)

    print(a)
    print(b)
    print(lc)
    print('--')

    out=["", ""]
    for e in na:
        out[0] += a[e]
        a = a[:e] + '-' + a[e+1:]
    for e in nb:
        out[1] += b[e]
        b = b[:e] + '-' + b[e+1:]

    a = a.replace('-', '')
    b = b.replace('-', '')

if len(a)>len(b):
    print(len(a))
else:
    print(len(b))
