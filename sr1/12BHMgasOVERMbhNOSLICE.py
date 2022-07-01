import pickle
import matplotlib.pyplot as plt 
import numpy as np 
file="acclog.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
yay=data['data']

bh0=yay[0]
Mgas0=yay[0]['Mgas']
cuMgas0 = np.cumsum(Mgas0)
time0=yay[0]['time']
Mbh0=yay[0]['Mbh']
cuMbh0 = np.cumsum(Mbh0)
ratio0=cuMgas0/Mbh0
newtime0=time0>0.5

bh1=yay[1]
Mgas1=yay[1]['Mgas']
cuMgas1 = np.cumsum(Mgas1)
time1=yay[1]['time']
Mbh1=yay[1]['Mbh']
cuMbh1 = np.cumsum(Mbh1)
ratio1=cuMgas1/Mbh1
newtime1=time1>0.5

bh5=yay[5]
Mgas5=yay[5]['Mgas']
cuMgas5 = np.cumsum(Mgas5)
time5=yay[5]['time']
Mbh5=yay[5]['Mbh']
cuMbh5 = np.cumsum(Mbh5)
ratio5=cuMgas5/Mbh5
newtime5=time5>0.255

bh8=yay[8]
Mgas8=yay[8]['Mgas']
cuMgas8 = np.cumsum(Mgas8)
time8=yay[8]['time']
Mbh8=yay[8]['Mbh']
cuMbh8 = np.cumsum(Mbh8)
ratio8=cuMgas8/Mbh8
newtime8=time8>0.3

bh11=yay[11]
Mgas11=yay[11]['Mgas']
cuMgas11 = np.cumsum(Mgas11)
time11=yay[11]['time']
Mbh11=yay[11]['Mbh']
cuMbh11 = np.cumsum(Mbh11)
ratio11=cuMgas11/Mbh11
newtime11=time11>0.315

bh13=yay[13]
Mgas13=yay[13]['Mgas']
cuMgas13 = np.cumsum(Mgas13)
time13=yay[13]['time']
Mbh13=yay[13]['Mbh']
cuMbh13 = np.cumsum(Mbh13)
ratio13=cuMgas13/Mbh13
newtime13=time13>0.272

bh15=yay[15]
Mgas15=yay[15]['Mgas']
cuMgas15 = np.cumsum(Mgas15)
time15=yay[15]['time']
Mbh15=yay[15]['Mbh']
cuMbh15 = np.cumsum(Mbh15)
ratio15=cuMgas15/Mbh15
newtime15=time15>0.31

bh16=yay[16]
Mgas16=yay[16]['Mgas']
cuMgas16 = np.cumsum(Mgas16)
time16=yay[16]['time']
Mbh16=yay[16]['Mbh']
cuMbh16 = np.cumsum(Mbh16)
ratio16=cuMgas16/Mbh16
newtime16=time16>0.304

bh17=yay[17]
Mgas17=yay[17]['Mgas']
cuMgas17 = np.cumsum(Mgas17)
time17=yay[17]['time']
Mbh17=yay[17]['Mbh']
cuMbh17 = np.cumsum(Mbh17)
ratio17=cuMgas17/Mbh17
newtime17=time17>0.305

bh37=yay[37]
Mgas37=yay[37]['Mgas']
cuMgas37 = np.cumsum(Mgas37)
time37=yay[37]['time']
Mbh37=yay[37]['Mbh']
cuMbh37 = np.cumsum(Mbh37)
ratio37=cuMgas37/Mbh37
newtime37=time37>0.36

bh38=yay[38]
Mgas38=yay[38]['Mgas']
cuMgas38 = np.cumsum(Mgas38)
time38=yay[38]['time']
Mbh38=yay[38]['Mbh']
cuMbh38 = np.cumsum(Mbh38)
ratio38=cuMgas38/Mbh38
newtime38=time38>0.359

bh43=yay[43]
Mgas43=yay[43]['Mgas']
cuMgas43 = np.cumsum(Mgas43)
time43=yay[43]['time']
Mbh43=yay[43]['Mbh']
cuMbh43 = np.cumsum(Mbh43)
ratio43=cuMgas43/Mbh43
newtime43=time43>0.5

fig,axis = plt.subplots(nrows=3,ncols=4)
axis[0, 0].plot(time0,ratio0)
axis[0, 0].set_xlabel('time (GYrs)')
axis[0, 0].set_ylabel('Cumulative Mgas/Mtotal')
axis[0, 0].title.set_text('BH0')

axis[0, 1].plot(time1,ratio1)
axis[0, 1].set_xlabel('time (GYrs)')
axis[0, 1].set_ylabel('Cumulative Mgas/Mtotal')
axis[0, 1].title.set_text('BH1')

axis[0, 2].plot(time5,ratio5)
axis[0, 2].set_xlabel('time (GYrs)')
axis[0, 2].set_ylabel('Cumulative Mgas/Mtotal')
axis[0, 2].title.set_text('BH5')

axis[0, 3].plot(time8,ratio8)
axis[0, 3].set_xlabel('time (GYrs)')
axis[0, 3].set_ylabel('Cumulative Mgas/Mtotal')
axis[0, 3].title.set_text('BH8')

axis[1, 0].plot(time11,ratio11)
axis[1, 0].set_xlabel('time (GYrs)')
axis[1, 0].set_ylabel('Cumulative Mgas/Mtotal')
axis[1, 0].title.set_text('BH11')

axis[1, 1].plot(time13,ratio13)
axis[1, 1].set_xlabel('time (GYrs)')
axis[1, 1].set_ylabel('Cumulative Mgas/Mtotal')
axis[1, 1].title.set_text('BH13')

axis[1, 2].plot(time15,ratio15)
axis[1, 2].set_xlabel('time (GYrs)')
axis[1, 2].set_ylabel('Cumulative Mgas/Mtotal')
axis[1, 2].title.set_text('BH15')

axis[1, 3].plot(time16,ratio16)
axis[1, 3].set_xlabel('time (GYrs)')
axis[1, 3].set_ylabel('Cumulative Mgas/Mtotal')
axis[1, 3].title.set_text('BH16')

axis[2, 0].plot(time17,ratio17)
axis[2, 0].set_xlabel('time (GYrs)')
axis[2, 0].set_ylabel('Cumulative Mgas/Mtotal')
axis[2, 0].title.set_text('BH17')

axis[2, 1].plot(time37,ratio37)
axis[2, 1].set_xlabel('time (GYrs)')
axis[2, 1].set_ylabel('Cumulative Mgas/Mtotal')
axis[2, 1].title.set_text('BH37')

axis[2, 2].plot(time38,ratio38)
axis[2, 2].set_xlabel('time (GYrs)')
axis[2, 2].set_ylabel('Cumulative Mgas/Mtotal')
axis[2, 2].title.set_text('BH38')

axis[2, 3].plot(time43,ratio43)
axis[2, 3].set_xlabel('time (GYrs)')
axis[2, 3].set_ylabel('Cumulative Mgas/Mtotal')
axis[2, 3].title.set_text('BH43')
plt.subplots_adjust(hspace=0.5,wspace=0.5)