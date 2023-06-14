import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt
file="sandra.orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
x=np.load('sandraxpos2.npy')
y=np.load('sandraypos2.npy')
z=np.load('sandrazpos2.npy')
sandratime=np.load('sandratime2.npy')
yay=data['data']
time=yay[8]['Time']
timeg=time.in_units('Gyr')
x0=yay[8]['x']
y0=yay[8]['y']
z0=yay[8]['z']
xi=np.interp(timeg,sandratime,x)
yi=np.interp(timeg,sandratime,y)
zi=np.interp(timeg,sandratime,z)
x9=yay[9]['x']
y9=yay[9]['y']
z9=yay[9]['z']
xc=x0[723:462103]
yc=y0[723:462103]
zc=z0[723:462103]
x9new=x9[:461380]
y9new=y9[:461380]
z9new=z9[:461380]
newx=x9new-xc
newy=y9new-yc
newz=z9new-zc
fig = plt.figure()
ax = plt.axes(projection='3d')
#ax.plot3D(newx,newy,newz)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.plot3D(xc,yc,zc)
ax.plot3D(x9new,y9new,z9new)
plt.show()