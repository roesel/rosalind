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
    worked_last_round = []
    worked = []
    tried_this_round = []

    best = ""

    for i in range(1, len(a)):
        print(i)
        combs = combinations(a, i)
        for cc in combs:
            c = ''.join(cc)
            if (c not in tried_this_round) and ( (c[0:i-1] in worked_last_round) or i==1 ):
                if is_subseq(c, b):
                    worked.append(c)
                tried_this_round.append(c)
        if not worked:
            return best
        else:
            best = worked[0]
            tried_this_round = []
            worked_last_round = worked
            worked = []




print("returning: "+find_lcsq(a, b))
