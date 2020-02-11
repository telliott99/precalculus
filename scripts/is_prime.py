import sys

def first_prime_factor(n,pL):
    for p in pL:
        if n % p == 0:
            return p, n/p
    return 1,n

def get_primes(N):
    pL = [2,3]
    for n in range(4, N+1):
        if first_prime_factor(n,pL)[0] == 1:
            pL.append(n)
    return pL

def fmt(L):
    rL = list()
    while L:
        sL = L[:8]
        L = L[8:]
        sL = [str(e).rjust(5) for e in sL]
        rL.append(''.join(sL))
    return '\n'.join(rL)

def check_if_prime(m,do_print=False):
    N = int(m**0.5)
    pL = get_primes(N)
    if do_print:
        print(fmt(pL))
    t = first_prime_factor(m,pL)
    print(t)

if __name__ == "__main__":
    m = int(sys.argv[1])
    check_if_prime(m)
    
    
    