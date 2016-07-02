from __future__ import division
import inspect
rid = inspect.getfile(inspect.currentframe()).replace('.py', '')

def get_params():
    with open('rosalind_'+rid+'.txt', 'r') as datafile:
        for line in datafile:
            return line.split(" ")[0], line.split(" ")[1] 

def fib(n, k, r, p):
    #print("After week "+str(n+1)+" there were "+str(p)+" reproducable rabbits and "+str(p+r*k)+" rabbits total.")    
    return n+1, k, p, p+r*k, r*k

def cycle(n_max, m, k=1):
    n = 1
    r = 0
    p = 1
    borns = [1]
    #print("On week "+str(n)+" there were "+str(r)+" reproducable rabbits and "+str(p-r)+" young rabbits.")                        
    while n<n_max:
        n, k, r, p, born = fib(n, k, r, p)

        born_m_back = 0
        if (n>m):
            born_m_back = borns[n-m-1]
        r, p = r-born_m_back, p-born_m_back                        
        #print("On week "+str(n)+" there were "+str(r)+" reproducable rabbits and "+str(p-r)+" young rabbits.")                
        #print str(born)+" rabbits were born."
        #print str(born_m_back)+" rabbits died."        
        borns.append(born)      
    return p

n, m = get_params()
#n, m = "6", "3"
#print "n = "+n
#print "k = "+k
print cycle(int(n), int(m))

            
