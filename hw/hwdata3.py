import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
from scipy import stats
file=np.loadtxt('data3.txt')
counts, edges, plot=plt.hist(file,bins=13)
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
plt.show()