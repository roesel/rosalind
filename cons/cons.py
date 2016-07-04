# http://rosalind.info/problems/cons/

# importing data
dataset = open('C:/Users/roese/Downloads/rosalind_cons.txt').read().strip().split()

for i in range(len(dataset)):
    if dataset[i][0] == ">":
        dataset[i] = "-"

del dataset[0]
ds = ''.join(dataset)
dataset = ds.split('-')

import numpy as np

m = np.zeros( (4, len(dataset[0])), dtype=np.int )

l = ["A", "C", "G", "T"]

for i in range(0, 4):
    for line in dataset:
        for j in range(0, len(line)):
            if line[j]==l[i]:
                m[i][j] += 1

out = ""
for i in np.argmax(m, axis=0):
    out += l[i]
print(out)

for i in range(0, 4):
    out = l[i]+": "
    for j in range(0, len(line)):
        out += str(m[i][j]) + " "
    print(out[:-1])
