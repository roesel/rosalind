# http://rosalind.info/problems/grph/
# importing data
dataset = open('C:/Users/roese/Downloads/rosalind_grph.txt').read().strip().split()

names = []
for i in range(len(dataset)):
    if dataset[i][0] == ">":
        names.append(dataset[i][1:])
        dataset[i] = "-"

del dataset[0]
ds = ''.join(dataset)
dataset = ds.split('-')


out = ""
for i in range(len(dataset)):
    for j in range(len(dataset)):
        if dataset[i] != dataset[j]:
            if dataset[i][-3:] == dataset[j][0:3]:
                out += names[i]+" "+names[j]+"\n"

print(out)
