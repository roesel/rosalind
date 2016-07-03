# http://rosalind.info/problems/lcsq/

from itertools import combinations

# importing data
dataset = open('C:/Users/roese/Downloads/rosalind_lcsq.txt').read().strip().split()

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
    i,j = len(a), len(b)
    while i*j != 0:
        if M[i][j] == M[i-1][j]:
            i -= 1
        elif M[i][j] == M[i][j-1]:
            j -= 1
        else:
            longest_sseq = a[i-1] + longest_sseq
            i -= 1
            j -= 1

    return longest_sseq


print(lcsq(a, b))
