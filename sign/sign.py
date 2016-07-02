from itertools import permutations, product

# stolen for python-ness, but understood
def plusAndMinusPermutations(items):
    for p in permutations(items):
        for signs in product([-1,1], repeat=len(items)):
            yield [a*sign for a,sign in zip(p,signs)]
n=6
items = [i for i in range(1,n+1)]

out = ''
f = 0
for p in plusAndMinusPermutations(items):
    f += 1
    for j in p:
        out += str(j)+' '
    out += '\n'
out = str(f)+'\n'+out

f = open('sign_out.txt','w')
f.write(out)
f.close()
