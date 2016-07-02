#http://rosalind.info/problems/lia/
from math import factorial as f

def P(k, n, p):
    ''' Binomial distribution (independent tries). '''
    return f(n)/f(k)/f(n-k)*p**k*(1-p)**(n-k)

def a(k, N):
    ''' One minus sum of all undesired outcomes. '''
    return round(1 - sum([P(n, 2**k, 0.25) for n in range(N)]), 3)

print(a(7, 37))
