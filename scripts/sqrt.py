import sys
s = int(sys.argv[1])

def next(n):
    n*= 10
    e = (len(str(n))-1) * 2
    t = s * 10**e
    
    m = n
    for i in range(10):
        m += 1
        if m**2 > t:
            break
    return m - 1

n = 1
for i in range(25):
    n = next(n)

print n

'''
> python sqrt2.py 2
14142135623730950488016887
> python sqrt2.py 3
17320508075688772935274463
>
'''