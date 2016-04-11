import numpy as np

dd = np.arange(1,21,1)
dd = dd[::-1]


for i,d in enumerate(dd): 
    print d
    if i == 0:
        total = d
    else:
        total+=d

print total
