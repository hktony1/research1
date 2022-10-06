import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
from scipy import stats
from sklearn.utils import shuffle
import random
import statistics
file=np.loadtxt('data1.txt')
plt.figure()
counts, edges, plot=plt.hist(file,bins=20)
mean=np.sum(file)/len(file)
print("The mean is", mean)
sort=np.sort(file)
v=(len(file)-1)/2
median=sort[int(v)]
print("The median is", median)
skew=sc.stats.skew(file)
print("The skew is", skew)
kurtosis=sc.stats.kurtosis(file)
print("The kurtosis is", kurtosis)
np.sort(counts)
data1_ind=np.unravel_index(np.argmax(counts), counts.shape)
print("The mode is", edges[data1_ind])
means=[]
for i in range(0,10000):
    random.shuffle(file)
    x=file[0:40]
    q=np.average(x)
    means.append(q)
array=np.array(means)
print(array)
standarad=statistics.stdev(array)
print("This is the standard deviation",standarad)
plt.figure()
plt.hist(array,bins=30)
plt.show()
