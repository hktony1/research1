import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt
#ruth merger 1 
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
x8=yay[8]['x']
y8=yay[8]['y']
z8=yay[8]['z']
xc=x0[580000:982864]
yc=y0[580000:982864]
zc=z0[580000:982864]
x8new=x8[578196:]
y8new=y8[578196:]
z8new=z8[578196:]
newx=x8new-xc
newy=y8new-yc
newz=z8new-zc
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title("Rm1")
#ax.plot3D(newx,newy,newz)
ax.set_xlabel('x (kpc)')
ax.set_ylabel('y (kpc)')
ax.set_zlabel('z (kpc)')
ax.plot3D(xc,yc,zc,)
ax.plot3D(x8new,y8new,z8new)
plt.show()