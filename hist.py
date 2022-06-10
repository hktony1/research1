import matplotlib.pyplot as plt
import numpy as np
import pickle
import scipy.optimize as opt 
from astropy.table import QTable
import astropy.units as u

file = 'findBH.txt'

with open(file,'rb') as f:
    data = np.loadtxt(f)
bhid=data[:,1]
distance=data[:,3]
bh1=bhid[np.mod(np.arange(bhid.size),3)!=2]
d2=distance[np.mod(np.arange(distance.size),3)!=2]
x=np.log10(d2)
h,xmids,_ = plt.hist(x)
plt.xlabel('Distance from center')
plt.ylabel('frequency')
plt.show()