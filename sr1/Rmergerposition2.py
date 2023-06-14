import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt
#ruth merger 2
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
x5=yay[5]['x']
y5=yay[5]['y']
z5=yay[5]['z']
xc=xi[46417:97317]
yc=yi[46417:97317]
zc=zi[46417:97317]
x5new=x5[45000:95900]
y5new=y5[45000:95900]
z5new=z5[45000:95900]
newx=x5new-xc
newy=y5new-yc
newz=z5new-zc
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_title("Rm2")
#ax.plot3D(newx,newy,newz)
ax.set_xlabel('x (kpc)')
ax.set_ylabel('y (kpc)')
ax.set_zlabel('z (kpc)')
ax.plot3D(xc,yc,zc,)
ax.plot3D(x5new,y5new,z5new)
plt.show()