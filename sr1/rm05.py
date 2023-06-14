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
fig = plt.figure()
"""ax = plt.axes(projection='3d')
ax.set_title("Rm1")
ax.set_xlabel('x (kpc)')
ax.set_ylabel('y (kpc)')
ax.set_zlabel('z (kpc)')
ax.plot3D(xc,yc,zc,)
ax.plot3D(x5new,y5new,z5new)
plt.show()"""
plt.plot(time,distance)
"""plt.scatter(tp,dp,s=20,marker="x")
plt.scatter(td,dd,s=20)"""
plt.xlabel('Time (Gyr)',fontsize=20)
plt.ylabel('Distance from merging black hole (kpc)',fontsize=20)
plt.title('Distance from merging black hole over time (0-5)', fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()