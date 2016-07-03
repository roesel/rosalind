from itertools import product

# importing data
dataset = open('C:/Users/roese/Downloads/rosalind_kmer.txt').read().strip().split()

for i in range(len(dataset)):
    if dataset[i][0] == ">":
        dataset[i] = "-"

del dataset[0]
ds = ''.join(dataset)
dataset = ds.split('-')

a = dataset[0]

def occurrences(string, sub):
    ''' like str.count() but dealing well with overlapping strings '''
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count+=1
        else:
            return count

n = 4
letters = "ACGT"
kmers = []
permutations = list(product(letters, repeat=n))
for p in permutations:
    strmer = ""
    for i in p:
        strmer = strmer + i
    kmers.append(strmer)

out = ""
for kmer in kmers:
    out += str(occurrences(a, kmer))+" "

print(out[:-1])  # trim last space
