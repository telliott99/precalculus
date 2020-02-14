# Courant's prime generator
# this builds a list of primes
# then tests whether i**2 - i + n is prime
# largest such number is 41
# 2 3 5 11 17 41 

import math

n = int(10e6)
L = [False] + [True] * n

MAX = int(math.sqrt(n))
for i in range(2,MAX):
    f = i
    while f < MAX + 1:
        f += i
        L[f] = False

pL = [i for i,n in enumerate(L) if n is True]

def test(n):
    for i in range(n):
        result = i**2 - i + n
        if not result in pL:
            return
    print n

for j in range(2,2500):
    test(j)
