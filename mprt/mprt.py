# http://rosalind.info/problems/orf/
# importing data
dataset = open('C:/Users/roese/Downloads/rosalind_mprt.txt').read().strip().split()

import urllib.request

ids = dataset
cds = []

for i in ids:
    url = 'http://www.uniprot.org/uniprot/uniprot_id.fasta'.replace('uniprot_id', i)
    response = urllib.request.urlopen(url)
    data = response.read()      # a `bytes` object
    text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
    r = text.split('\n')[1:]
    s = ''.join(r)
    cds.append(s)

def is_N(p, s):
    if s[p+1] != "P" and (s[p+2] == "S" or s[p+2] == "T") and s[p+3] != "P":
        return True
    else:
        return False

import re
p=""
for i in range(len(ids)):
    f = re.finditer(r'N', cds[i])
    out = ""
    for match in f:
        if is_N(match.start(), cds[i]):
            out += str(match.start()+1)+" "
    if out[:-1]:
        p += ids[i]+"\n"
        p += out[:-1]+"\n"

print(p)
