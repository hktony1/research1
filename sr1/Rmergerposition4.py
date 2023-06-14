import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt
#ruth merger 4
file="orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
x=np.load('x2.npy')
y=np.load('y2.npy')
z=np.load('z2.npy')
yay=data['data']
time=yay[1]['Time']
x1=yay[1]['x']
y1=yay[1]['y']
z1=yay[1]['z']
xi=np.interp(x1,x,x)
yi=np.interp(x1,x,y)
zi=np.interp(x1,x,z)
x37=yay[37]['x']
y37=yay[37]['y']
z37=yay[37]['z']
xc=xi[8585:519996]
yc=yi[8585:519996]
zc=zi[8585:519996]
x37new=x37[:511411]
y37new=y37[:511411]
z37new=z37[:511411]
newx=x37new-xc
newy=y37new-yc
newz=z37new-zc
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title("Rm4")
#ax.plot3D(newx,newy,newz)
ax.set_xlabel('x (kpc)')
ax.set_ylabel('y (kpc)')
ax.set_zlabel('z (kpc)')
ax.plot3D(xc,yc,zc,)
ax.plot3D(x37new,y37new,z37new)
plt.show()