from __future__ import division
import inspect
rid = inspect.getfile(inspect.currentframe()).replace('.py', '')

def get_params():
    with open('rosalind_'+rid+'.txt', 'r') as datafile:
        for line in datafile:
            return line.split(" ")[0], line.split(" ")[1] 

def fib(n, k, r, p):
    #print("After week "+str(n+1)+" there were "+str(p)+" reproducable rabbits and "+str(p+r*k)+" rabbits total.")    
    return n+1, k, p, p+r*k

def cycle(n_max, k):
    n = 1
    r = 0
    p = 1
    while n<n_max:
        n, k, r, p = fib(n, k, r, p)      
    return p

n, k = get_params()
#print "n = "+n
#print "k = "+k
print cycle(int(n), int(k))

            
