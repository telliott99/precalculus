def load(fn):
    fh = open(fn, 'r')
    data = fh.read()
    fh.close()
    return data
    
def get_fn(s):
    j = s.find('png')
    i = 0
    k = s.find('{',i)
    while k < j:
        i = k
        k = s.find('{', k+1)
        if k == -1:
            break
    return s[i+1:j+3]

def filter(e):
    if '.png' in e:  return True
    if '.jpg' in e:  return True
    return False
    
def get_fig_fn(s):
    L = s.strip().split('\n')
    L = [e.strip() for e in L]
    L = [e for e in L if filter(e)]
    L = [e for e in L if not e[0] == '%']
    L = [get_fn(e) for e in L]
    return L    
