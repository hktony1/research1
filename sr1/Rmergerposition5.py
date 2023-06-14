import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt
#ruth merger 5
file="orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
x=np.load('x2.npy')
y=np.load('y2.npy')
z=np.load('z2.npy')
yay=data['data']
time=yay[10]['Time']
x10=yay[10]['x']
y10=yay[10]['y']
z10=yay[10]['z']
xi=np.interp(x10,x,x)
yi=np.interp(x10,x,y)
zi=np.interp(x10,x,z)
x39=yay[39]['x']
y39=yay[39]['y']
z39=yay[39]['z']
xc=xi[56679:78820]
yc=yi[56679:78820]
zc=zi[56679:78820]
x39new=x39[50000:72141]
y39new=y39[50000:72141]
z39new=z39[50000:72141]
newx=x39new-xc
newy=y39new-yc
newz=z39new-zc
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title("Rm5")
#ax.plot3D(newx,newy,newz)
ax.set_xlabel('x (kpc)')
ax.set_ylabel('y (kpc)')
ax.set_zlabel('z (kpc)')
ax.plot3D(xc,yc,zc,)
ax.plot3D(x39new,y39new,z39new)
plt.show()