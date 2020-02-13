import os
import util
from shutil import copyfile

opath = '/Users/telliott/Github/precalculus/'
ipath = '/Users/telliott/Github/calculus_book/'

p = opath + 'files'

#----------------

L = os.listdir(p)
L.sort()

for fn in L:
    print(fn)
    data = util.load(p + '/' + fn)
    sL = util.get_fig_fn(data)
    for e in sL:
        print(e)
    print


