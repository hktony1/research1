import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt
import scipy as sc
from scipy.signal import argrelextrema
file="sandra.orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
yay=data['data']
t0=yay[0]['Time']
time0=t0.in_units('Gyr')
time=time0[134411:761503]
x0=yay[0]['x']
y0=yay[0]['y']
z0=yay[0]['z']
x8=yay[8]['x']
y8=yay[8]['y']
z8=yay[8]['z']
xc=x0[134411:761503]
yc=y0[134411:761503]
zc=z0[134411:761503]
x8new=x8[133076:760168]
y8new=y8[133076:760168]
z8new=z8[133076:760168]
x=x8new-xc
y=y8new-yc
z=z8new-zc
distance=np.sqrt(x**2+y**2+z**2)
peaks=argrelextrema(distance, np.greater, order=4000)
dips=argrelextrema(distance, np.less, order=5000)
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
ax.plot3D(x8new,y8new,z8new)
plt.show()"""
plt.plot(time,distance)
plt.scatter(tp,dp,s=20,marker="x")
plt.scatter(td,dd,s=20)
plt.xlabel('Time (Gyr)',fontsize=20)
plt.ylabel('Distance (kpc)',fontsize=20)
plt.title('Distance from Halo Center', fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()