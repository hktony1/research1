import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt
import scipy as sc
from scipy.signal import argrelextrema
file="elena.orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
yay=data['data']
t1=yay[1]['Time']
time1=t1.in_units('Gyr')
time=time1[110598:205166]
x1=yay[1]['x']
y1=yay[1]['y']
z1=yay[1]['z']
x2=yay[2]['x']
y2=yay[2]['y']
z2=yay[2]['z']
xc=x1[110598:205166]
yc=y1[110598:205166]
zc=z1[110598:205166]
x2new=x2[106319:200887]
y2new=y2[106319:200887]
z2new=z2[106319:200887]
x=x2new-xc
y=y2new-yc
z=z2new-zc
distance=np.sqrt(x**2+y**2+z**2)
peaks=argrelextrema(distance, np.greater, order=4300)
dips=argrelextrema(distance, np.less, order=3000)
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
ax.plot3D(x2new,y2new,z2new)
plt.show()"""
plt.plot(time,distance)
plt.scatter(tp,dp,s=20,marker="x")
plt.scatter(td,dd,s=20)
plt.xlabel('Time (Gyr)',fontsize=20)
plt.ylabel('Distance from merging black hole (kpc)',fontsize=20)
plt.title('Distance from merging black hole over time (1-2)', fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()