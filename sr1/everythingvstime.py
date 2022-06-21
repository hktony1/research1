import pickle
import matplotlib.pyplot as plt 
import numpy as np 
file="orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
yay=data['data']
time=yay[0]['Time']
mass=yay[0]['mass']
E=yay[0]['E']
x=yay[0]['x']
y=yay[0]['y']
z=yay[0]['z']
vx=yay[0]['vx']
vy=yay[0]['vy']
vz=yay[0]['vz']
pot=yay[0]['pot']
mdot=yay[0]['mdot']
dM=yay[0]['dM']
dt=yay[0]['dt']
redshift=yay[0]['redshift']
fig,axis = plt.subplots(nrows=3,ncols=4)
axis[0, 0].plot(time,mass)
axis[0, 0].set_xlabel('time')
axis[0, 0].set_ylabel('mass')
axis[0, 1].plot(time,x)
axis[0, 1].set_xlabel('time')
axis[0, 1].set_ylabel('x')
axis[0, 2].plot(time,vx)
axis[0, 2].set_xlabel('time')
axis[0, 2].set_ylabel('vx')
axis[0, 3].plot(time,mdot)
axis[0, 3].set_xlabel('time')
axis[0, 3].set_ylabel('mdot')
axis[1, 0].plot(time,pot)
axis[1, 0].set_xlabel('time')
axis[1, 0].set_ylabel('pot')
axis[1, 1].plot(time,y)
axis[1, 1].set_xlabel('time')
axis[1, 1].set_ylabel('y')
axis[1, 2].plot(time,vy)
axis[1, 2].set_xlabel('time')
axis[1, 2].set_ylabel('vy')
axis[1, 3].plot(time,dM)
axis[1, 3].set_xlabel('time')
axis[1, 3].set_ylabel('dM')
axis[2, 0].plot(time,redshift)
axis[2, 0].set_xlabel('time')
axis[2, 0].set_ylabel('redshift')
axis[2, 1].plot(time,z)
axis[2, 1].set_xlabel('time')
axis[2, 1].set_ylabel('z')
axis[2, 2].plot(time,vz)
axis[2, 2].set_xlabel('time')
axis[2, 2].set_ylabel('vz')
axis[2, 3].plot(time,dt)
axis[2, 3].set_xlabel('time')
axis[2, 3].set_ylabel('dt')

