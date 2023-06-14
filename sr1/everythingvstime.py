import pickle
import matplotlib.pyplot as plt 
import numpy as np 
#this is how to laod a pickle file
file="orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
#i call all my pickle data yay
yay=data['data']
#time data for black hole 0
time=yay[0]['Time']
#mass data for black hole 0
mass=yay[0]['mass']
#all sorts of data in yay[0] you can do yay[0].keys to see what kind of data is in yay[0]
#we log stuff sometimes to help visualize the graph easier
logmass=np.log10(mass)
E=yay[0]['E']
x=yay[0]['x']
y=yay[0]['y']
z=yay[0]['z']
vx=yay[0]['vx']
vy=yay[0]['vy']
vz=yay[0]['vz']
pot=yay[0]['pot']
mdot=yay[0]['mdot']
logmdot=np.log10(mdot)
dM=yay[0]['dM']
logdM=np.log10(dM)
dt=yay[0]['dt']
redshift=yay[0]['redshift']
#subplots axis[number,number] is just the position of each subplot
fig,axis = plt.subplots(nrows=3,ncols=4)
axis[0, 0].plot(time,logmass)
axis[0, 0].set_xlabel('time')
axis[0, 0].set_ylabel('mass')
axis[0, 1].plot(time,x)
axis[0, 1].set_xlabel('time')
axis[0, 1].set_ylabel('x')
axis[0, 2].plot(time,vx)
axis[0, 2].set_xlabel('time')
axis[0, 2].set_ylabel('vx')
axis[0, 3].plot(time,logmdot)
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
axis[1, 3].plot(time,logdM)
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
plt.subplots_adjust(hspace=0.5,wspace=0.5)
plt.show()