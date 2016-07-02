from __future__ import division
import inspect
rid = inspect.getfile(inspect.currentframe()).replace('.py', '').split('/')[-1]

import itertools

def get_params():
    with open('rosalind_'+rid+'.txt', 'r') as datafile:
        for line in datafile:
            return line.split(" ")[0]

n = int(get_params())

numbers = [i for i in range(1, n+1)]
permutations = list(itertools.permutations(numbers, n))

with open('rosalind_'+rid+'_output.txt', 'a') as output:
    output.seek(0)
    output.truncate()
    output.write(str(len(permutations))+'\n')
    for permutation in permutations:
        output.write( ' '.join([str(i) for i in permutation]) + '\n')



#print list(itertools.permutations([1,2,3,4], 2))
##n, m = "6", "3"
##print "n = "+n
##print "k = "+k
#print cycle(int(n), int(m))
#
#
