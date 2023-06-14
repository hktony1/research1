import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt
#ruth merger 3
file="orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
x=np.load('xposition.npy')
y=np.load('yposition.npy')
z=np.load('zposition.npy')
yay=data['data']
time=yay[0]['Time']
x0=yay[0]['x']
y0=yay[0]['y']
z0=yay[0]['z']
xi=np.interp(x0,x,x)
yi=np.interp(x0,x,y)
zi=np.interp(x0,x,z)
x22=yay[22]['x']
y22=yay[22]['y']
z22=yay[22]['z']
xc=xi[5997:324949]
yc=yi[5997:324949]
zc=zi[5997:324949]
x22new=x22[:318952]
y22new=y22[:318952]
z22new=z22[:318952]
newx=x22new-xc
newy=y22new-yc
newz=z22new-zc
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title("Rm3")
#ax.plot3D(newx,newy,newz)
ax.set_xlabel('x (kpc)')
ax.set_ylabel('y (kpc)')
ax.set_zlabel('z (kpc)')
ax.plot3D(xc,yc,zc,)
ax.plot3D(x22new,y22new,z22new)
plt.show()