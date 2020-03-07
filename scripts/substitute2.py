# use python2
import os, util

targ = '\Large'
sub = '\Large\n\n%[my-super-duper-separator]'

d = '/Users/telliott/Github/precalculus/files'

for fn in os.listdir(d):
    path = '/'.join([d,fn])
    sL = list()
    data = util.load(path)
    
    for line in data.strip().split('\n'):
        if targ in line:
            line = line.replace(targ,sub)
        sL.append(line)
        
    fh = open(path,'w')
    fh.write('\n'.join(sL))
    fh.close()