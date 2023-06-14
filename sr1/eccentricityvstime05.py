import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt
import scipy as sc
from scipy.signal import argrelextrema
file="orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
yay=data['data']
t0=yay[0]['Time']
time0=t0.in_units('Gyr')
time=time0[48556:97317]
x0=yay[0]['x']
y0=yay[0]['y']
z0=yay[0]['z']
x5=yay[5]['x']
y5=yay[5]['y']
z5=yay[5]['z']
xc=x0[48556:97317]
yc=y0[48556:97317]
zc=z0[48556:97317]
x5new=x5[47139:95900]
y5new=y5[47139:95900]
z5new=z5[47139:95900]
x=x5new-xc
y=y5new-yc
z=z5new-zc
distance=np.sqrt(x**2+y**2+z**2)
peaks=argrelextrema(distance, np.greater, order=1000)
dips=argrelextrema(distance, np.less, order=1000)
dp=distance[peaks]
tp=time[peaks]
dd=distance[dips]
td=time[dips]
e=(dp-dd)/(dp+dd)
t=(tp+td)/2
fig = plt.figure()
plt.scatter(t,e)
plt.plot(t,e)
plt.xlabel('Time (Gyr)',fontsize=20)
plt.ylabel('Eccentricity',fontsize=20)
plt.title('Eccentricity of orbit over time (0-5)', fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()