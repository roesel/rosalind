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

def is_subseq(x, y):
    it = iter(y)
    return all(any(c == ch for c in it) for ch in x)

def find_lcsq(a, b):
    for i in range(0, len(a)):
        combs = combinations(a, len(a)-i)
        for c in combs:
            if is_subseq(''.join(c), b):
                return ''.join(c)

print(find_lcsq(a, b))
