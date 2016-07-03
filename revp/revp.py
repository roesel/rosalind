# http://rosalind.info/problems/revp/

# importing data
dataset = open('C:/Users/roese/Downloads/rosalind_revp.txt').read().strip().split()

for i in range(len(dataset)):
    if dataset[i][0] == ">":
        dataset[i] = "-"

del dataset[0]
ds = ''.join(dataset)
dataset = ds.split('-')

a = dataset[0]

def is_rev_pal(s):
    k = {'C':'G', 'G':'C', 'T':'A', 'A':'T'}
    transl = ""
    for letter in s:
        transl += k[letter]
    if transl == s[::-1]:
        return True
    else:
        return False

for i in range(0, len(a)):
    for j in range (4, 13):
        if is_rev_pal(a[i:i+j]) and len(a[i:i+j])==j:
            print(str(i+1)+" "+str(j))
