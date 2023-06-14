import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt
file="sandra.orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
x=np.load('sandraxpos3.npy')
y=np.load('sandraypos3.npy')
z=np.load('sandrazpos3.npy')
sandratime=np.load('sandratime3.npy')
yay=data['data']
time=yay[0]['Time']
timeg=time.in_units('Gyr')
x0=yay[0]['x']
y0=yay[0]['y']
z0=yay[0]['z']
xi=np.interp(timeg,sandratime,x)
yi=np.interp(timeg,sandratime,y)
zi=np.interp(timeg,sandratime,z)
x8=yay[8]['x']
y8=yay[8]['y']
z8=yay[8]['z']
xc=xi[1334:761502]
yc=yi[1334:761502]
zc=zi[1334:761502]
x8new=x8[:760168]
y8new=y8[:760168]
z8new=z8[:760168]
newx=x8new-xc
newy=y8new-yc
newz=z8new-zc
fig = plt.figure()
ax = plt.axes(projection='3d')
#ax.plot3D(newx,newy,newz)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot3D(xc,yc,zc)
ax.plot3D(x8new,y8new,z8new)
plt.show()