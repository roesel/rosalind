from __future__ import division
import inspect
rid = inspect.getfile(inspect.currentframe()).replace('.py', '').split('/')[-1]

import itertools

def get_params():
    strings = []
    with open('rosalind_'+rid+'.txt', 'r') as datafile:
        for line in datafile:
            strings.append(line.replace('\n', ''))
    return tuple(strings)

def is_ok(permutation):
    if ( permutation[0] != ' ' and permutation[1] != ' ' and permutation[2] != ' ' ):
        return True
    if ( permutation[0] != ' ' and permutation[1] != ' ' and permutation[2] == ' ' ):
        return True
    if ( permutation[0] != ' ' and permutation[1] == ' ' and permutation[2] == ' ' ):
        return True
    else:
        return False

params = get_params()

letters = params[0].replace(' ', '')
letters = ' '+letters
n = int(params[1])

#weights = [i for i in range(1, len(letters)+1)]

#database = dict(zip(weights, letters))
permutations = list(itertools.product(letters, repeat=n))

with open('rosalind_'+rid+'_output.txt', 'a') as output:
    output.seek(0)
    output.truncate()
    #output.write(str(len(permutations))+'\n')
    for permutation in permutations:
        if (is_ok(permutation)):
            output.write( ''.join([i for i in permutation]) + '\n')