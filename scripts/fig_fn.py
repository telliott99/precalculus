import os
import util
from shutil import copyfile

opath = '/Users/telliott/Github/precalculus/'
ipath = '/Users/telliott/Github/calculus_book/'

p = opath + 'files'

#----------------

L = os.listdir(p)
sL = []

for fn in L:
    data = util.load(p + '/' + fn)
    sL.extend(util.get_fig_fn(data))

sL = sorted(sL, key=lambda s: s.lower())

#----------------

for fn in sL:
    print fn
    continue
    src = ipath + 'png/' + fn
    dst = opath + 'fig/' + fn
    if not os.path.exists(dst):
        try:
            copyfile(src, dst)
        except IOError:
            pass