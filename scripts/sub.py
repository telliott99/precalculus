import os
import util
from shutil import copyfile

project = 'precalculus/'
sub = '\graphicspath{{/Users/telliott/Github/figures/}}'

path = '/Users/telliott/Github/' + project + 'files'
L = os.listdir(path)
L.sort()

for fn in L:
    if fn.startswith('.'):
        continue
    pL = list()
    print(fn)
    data = util.load(path + '/' + fn)
    data = data.strip().split('\n')
    for line in data:
        if line.startswith('\graphicspath'):
            pL.append(sub)
        else:
            pL.append(line)
    fh = open(path + '/' + fn, 'w')
    fh.write('\n'.join(pL))
    fh.close()

