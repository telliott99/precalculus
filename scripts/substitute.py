

import os, util

targ = '$\circ'
pre = 'circ'
sub = 'bullet'

d = '/Users/telliott/Github/precalculus/files'

for fn in os.listdir(d):
    path = '/'.join([d,fn])
    sL = list()
    data = util.load(path)
    
    for line in data.strip().split('\n'):
        if targ in line:
            if '^' + targ in line:
                continue
            line = line.replace(pre,sub)
        sL.append(line)
        
    fh = open(path,'w')
    fh.write('\n'.join(sL))
    fh.close()