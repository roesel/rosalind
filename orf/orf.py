# http://rosalind.info/problems/orf/
# importing data
dataset = open('C:/Users/roese/Downloads/rosalind_orf.txt').read().strip().split()

for i in range(len(dataset)):
    if dataset[i][0] == ">":
        dataset[i] = "-"

del dataset[0]
ds = ''.join(dataset)
dataset = ds.split('-')

inp = dataset[0]

def comple(s):
    '''Returns complementary DNA string.'''
    out = ""
    l = {"A":"T", "G":"C", "C":"G", "T":"A"}
    for c in s:
        out += l[c]
    return out


def to_amin(s):
    '''Converts DNA string to aminoacid codes.'''
    t = {
    # X for Stop codon
    "TTT":"F",      "CTT":"L",      "ATT":"I",      "GTT":"V",
    "TTC":"F",      "CTC":"L",      "ATC":"I",      "GTC":"V",
    "TTA":"L",      "CTA":"L",      "ATA":"I",      "GTA":"V",
    "TTG":"L",      "CTG":"L",      "ATG":"M",      "GTG":"V",
    "TCT":"S",      "CCT":"P",      "ACT":"T",      "GCT":"A",
    "TCC":"S",      "CCC":"P",      "ACC":"T",      "GCC":"A",
    "TCA":"S",      "CCA":"P",      "ACA":"T",      "GCA":"A",
    "TCG":"S",      "CCG":"P",      "ACG":"T",      "GCG":"A",
    "TAT":"Y",      "CAT":"H",      "AAT":"N",      "GAT":"D",
    "TAC":"Y",      "CAC":"H",      "AAC":"N",      "GAC":"D",
    "TAA":"X",      "CAA":"Q",      "AAA":"K",      "GAA":"E",
    "TAG":"X",      "CAG":"Q",      "AAG":"K",      "GAG":"E",
    "TGT":"C",      "CGT":"R",      "AGT":"S",      "GGT":"G",
    "TGC":"C",      "CGC":"R",      "AGC":"S",      "GGC":"G",
    "TGA":"X",      "CGA":"R",      "AGA":"R",      "GGA":"G",
    "TGG":"W",      "CGG":"R",      "AGG":"R",      "GGG":"G",
    }
    out = ""
    e = len(s) - (len(s)%3)
    for i in range(0, e, 3):
        out+=t[s[i:i+3]]
    return out

def look(s):
    '''Finds the substring from start to first stop codon.'''
    for i in range(len(s)):
        if s[i] == "X":
            return s[0:i]
    return ""

import re

strings = [inp, comple(inp[::-1])]
found = []
for s in strings:
    finds = re.findall(r'(?=(ATG.*))', s)
    for f in finds:
        match = look(to_amin(f))
        if match and match not in found:
            found.append(match)
            print(match)
