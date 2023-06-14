import pickle
import matplotlib.pyplot as plt 
import numpy as np
#this is how you load a pickle file 
file="acclog.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
#i like to call all my data yay
yay=data['data']
#yay[a number] is just a black hole there are 45 black holes in ruth so it goes from 0-44
#This is just a sub plot of ever black hole with over 1 million solar mass and its percentage of mass gained from accretion vs time
#cumsum is cumulative sum
#newtime is a way of slcing data sets
bh0=yay[0]
Mgas0=yay[0]['deltaMgas']
cuMgas0 = np.cumsum(Mgas0)
time0=yay[0]['time']
Mbh0=yay[0]['Mbh']
cuMbh0 = np.cumsum(Mbh0)
ratio0=cuMgas0/Mbh0
newtime0=time0>0.38

bh1=yay[1]
Mgas1=yay[1]['deltaMgas']
cuMgas1 = np.cumsum(Mgas1)
time1=yay[1]['time']
Mbh1=yay[1]['Mbh']
cuMbh1 = np.cumsum(Mbh1)
ratio1=cuMgas1/Mbh1
newtime1=time1>0.46

bh5=yay[5]
Mgas5=yay[5]['deltaMgas']
cuMgas5 = np.cumsum(Mgas5)
time5=yay[5]['time']
Mbh5=yay[5]['Mbh']
cuMbh5 = np.cumsum(Mbh5)
ratio5=cuMgas5/Mbh5
newtime5=time5>0.26

bh8=yay[8]
Mgas8=yay[8]['deltaMgas']
cuMgas8 = np.cumsum(Mgas8)
time8=yay[8]['time']
Mbh8=yay[8]['Mbh']
cuMbh8 = np.cumsum(Mbh8)
ratio8=cuMgas8/Mbh8
newtime8=time8>0.37

bh11=yay[11]
Mgas11=yay[11]['deltaMgas']
cuMgas11 = np.cumsum(Mgas11)
time11=yay[11]['time']
Mbh11=yay[11]['Mbh']
cuMbh11 = np.cumsum(Mbh11)
ratio11=cuMgas11/Mbh11
newtime11=time11>0.38

bh13=yay[13]
Mgas13=yay[13]['deltaMgas']
cuMgas13 = np.cumsum(Mgas13)
time13=yay[13]['time']
Mbh13=yay[13]['Mbh']
cuMbh13 = np.cumsum(Mbh13)
ratio13=cuMgas13/Mbh13
newtime13=time13>0.272

bh15=yay[15]
Mgas15=yay[15]['deltaMgas']
cuMgas15 = np.cumsum(Mgas15)
time15=yay[15]['time']
Mbh15=yay[15]['Mbh']
cuMbh15 = np.cumsum(Mbh15)
ratio15=cuMgas15/Mbh15
newtime15=time15>0.31

bh16=yay[16]
Mgas16=yay[16]['deltaMgas']
cuMgas16 = np.cumsum(Mgas16)
time16=yay[16]['time']
Mbh16=yay[16]['Mbh']
cuMbh16 = np.cumsum(Mbh16)
ratio16=cuMgas16/Mbh16
newtime16=time16>0.304

bh17=yay[17]
Mgas17=yay[17]['deltaMgas']
cuMgas17 = np.cumsum(Mgas17)
time17=yay[17]['time']
Mbh17=yay[17]['Mbh']
cuMbh17 = np.cumsum(Mbh17)
ratio17=cuMgas17/Mbh17
newtime17=time17>0.305

bh37=yay[37]
Mgas37=yay[37]['deltaMgas']
cuMgas37 = np.cumsum(Mgas37)
time37=yay[37]['time']
Mbh37=yay[37]['Mbh']
cuMbh37 = np.cumsum(Mbh37)
ratio37=cuMgas37/Mbh37
newtime37=time37>0.36

bh38=yay[38]
Mgas38=yay[38]['deltaMgas']
cuMgas38 = np.cumsum(Mgas38)
time38=yay[38]['time']
Mbh38=yay[38]['Mbh']
cuMbh38 = np.cumsum(Mbh38)
ratio38=cuMgas38/Mbh38
newtime38=time38>0.366

bh43=yay[43]
Mgas43=yay[43]['deltaMgas']
cuMgas43 = np.cumsum(Mgas43)
time43=yay[43]['time']
Mbh43=yay[43]['Mbh']
cuMbh43 = np.cumsum(Mbh43)
ratio43=cuMgas43/Mbh43
newtime43=time43>0.5
#this is just the subplots axis[number,number] is just the position of the subplot
fig,axis = plt.subplots(nrows=3,ncols=4)
axis[0, 0].plot(time0[newtime0],ratio0[newtime0])
axis[0, 0].set_xlabel('Time (GYrs)')
axis[0, 0].set_ylabel('Gas Accreted/Total Mass')
axis[0, 0].title.set_text('BH0')

axis[0, 1].plot(time1[newtime1],ratio1[newtime1])
axis[0, 1].set_xlabel('Time (GYrs)')
axis[0, 1].set_ylabel('Gas Accreted/Total Mass')
axis[0, 1].title.set_text('BH1')

axis[0, 2].plot(time5[newtime5],ratio5[newtime5])
axis[0, 2].set_xlabel('Time (GYrs)')
axis[0, 2].set_ylabel('Gas Accreted/Total Mass')
axis[0, 2].title.set_text('BH5')

axis[0, 3].plot(time8[newtime8],ratio8[newtime8])
axis[0, 3].set_xlabel('Time (GYrs)')
axis[0, 3].set_ylabel('Gas Accreted/Total Mass')
axis[0, 3].title.set_text('BH8')

axis[1, 0].plot(time11[newtime11],ratio11[newtime11])
axis[1, 0].set_xlabel('Time (GYrs)')
axis[1, 0].set_ylabel('Gas Accreted/Total Mass')
axis[1, 0].title.set_text('BH11')

axis[1, 1].plot(time13[newtime13],ratio13[newtime13])
axis[1, 1].set_xlabel('Time (GYrs)')
axis[1, 1].set_ylabel('Gas Accreted/Total Mass')
axis[1, 1].title.set_text('BH13')

axis[1, 2].plot(time15[newtime15],ratio15[newtime15])
axis[1, 2].set_xlabel('Time (GYrs)')
axis[1, 2].set_ylabel('Gas Accreted/Total Mass')
axis[1, 2].title.set_text('BH15')

axis[1, 3].plot(time16[newtime16],ratio16[newtime16])
axis[1, 3].set_xlabel('Time (GYrs)')
axis[1, 3].set_ylabel('Gas Accreted/Total Mass')
axis[1, 3].title.set_text('BH16')

axis[2, 0].plot(time17[newtime17],ratio17[newtime17])
axis[2, 0].set_xlabel('Time (GYrs)')
axis[2, 0].set_ylabel('Gas Accreted/Total Mass')
axis[2, 0].title.set_text('BH17')

axis[2, 1].plot(time37[newtime37],ratio37[newtime37])
axis[2, 1].set_xlabel('Time (GYrs)')
axis[2, 1].set_ylabel('Gas Accreted/Total Mass')
axis[2, 1].title.set_text('BH37')

axis[2, 2].plot(time38[newtime38],ratio38[newtime38])
axis[2, 2].set_xlabel('Time (GYrs)')
axis[2, 2].set_ylabel('Gas Accreted/Total Mass')
axis[2, 2].title.set_text('BH38')

axis[2, 3].plot(time43[newtime43],ratio43[newtime43])
axis[2, 3].set_xlabel('Time (GYrs)')
axis[2, 3].set_ylabel('Gas Accreted/Total Mass')
axis[2, 3].title.set_text('BH43')
plt.subplots_adjust(hspace=0.5,wspace=0.5)
plt.show()