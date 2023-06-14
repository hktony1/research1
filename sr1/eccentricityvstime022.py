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
time=time0[6913:324949]
x0=yay[0]['x']
y0=yay[0]['y']
z0=yay[0]['z']
x22=yay[22]['x']
y22=yay[22]['y']
z22=yay[22]['z']
xc=x0[6913:324949]
yc=y0[6913:324949]
zc=z0[6913:324949]
x22new=x22[916:318952]
y22new=y22[916:318952]
z22new=z22[916:318952]
x=x22new-xc
y=y22new-yc
z=z22new-zc
distance=np.sqrt(x**2+y**2+z**2)
peaks=argrelextrema(distance, np.greater, order=1600)
dips=argrelextrema(distance, np.less, order=1600)
dp=distance[peaks][0:65]
tp=time[peaks][0:65]
dd=distance[dips][0:65]
td=time[dips][0:65]
e=(dp-dd)/(dp+dd)
t=(tp+td)/2
fig = plt.figure()
plt.scatter(t,e)
plt.plot(t,e)
plt.xlabel('Time (Gyr)',fontsize=20)
plt.ylabel('Eccentricity',fontsize=20)
plt.title('Eccentricity of orbit over time (0-22)', fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()