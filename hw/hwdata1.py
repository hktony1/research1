import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
from scipy import stats
from sklearn.utils import shuffle
import random
import statistics
file=np.loadtxt('data1.txt')
file2=np.loadtxt('data2.txt')
file3=np.loadtxt('data3.txt')
#data1
plt.figure()
counts, edges, plot=plt.hist(file,bins=20)
plt.title('Data1')
mean=np.sum(file)/len(file)
print("The mean for data1 is", mean)
sort=np.sort(file)
v=(len(file)-1)/2
median=sort[int(v)]
print("The median for data1 is", median)
skew=sc.stats.skew(file)
print("The skew for data1 is", skew)
kurtosis=sc.stats.kurtosis(file)
print("The kurtosis for data1 is", kurtosis)
np.sort(counts)
data1_ind=np.unravel_index(np.argmax(counts), counts.shape)
print("The mode for data1 is", edges[data1_ind])
means=[]
for i in range(0,10000):
    random.shuffle(file)
    x=file[0:40]
    q=np.average(x)
    means.append(q)
array=np.array(means)
standarad=statistics.stdev(array)
print("This is the standard deviation for data1",standarad)
plt.figure()
plt.hist(array,bins=30)
plt.title('Normal Data1')
#data2
plt.figure()
counts2, edges2, plot2=plt.hist(file2,bins=20)
plt.title('Data2')
mean2=np.sum(file2)/len(file2)
print("The mean for data2 is", mean2)
sort2=np.sort(file2)
v2=(len(file2)-1)/2
median2=sort2[int(v2)]
print("The median for data2 is", median2)
skew2=sc.stats.skew(file2)
print("The skew for data2 is", skew2)
kurtosis2=sc.stats.kurtosis(file2)
print("The kurtosis for data2 is", kurtosis2)
np.sort(counts2)
data1_ind2=np.unravel_index(np.argmax(counts2), counts2.shape)
print("The mode for data2 is", edges2[data1_ind2])
means2=[]
for j in range(0,10000):
    random.shuffle(file2)
    x2=file2[0:40]
    q2=np.average(x2)
    means2.append(q2)
array2=np.array(means2)
standarad2=statistics.stdev(array2)
print("This is the standard deviation for data2",standarad2)
plt.figure()
plt.hist(array2,bins=30)
plt.title('Normal Data2')
#Data3
plt.figure()
counts3, edges3, plot3=plt.hist(file3,bins=13)
plt.title('Data3')
mean3=np.sum(file3)/len(file3)
print("The mean for data3 is", mean3)
sort3=np.sort(file3)
v3=(len(file3)-1)/2
median3=sort3[int(v3)]
print("The median for data3 is", median3)
skew3=sc.stats.skew(file3)
print("The skew for data3 is", skew3)
kurtosis3=sc.stats.kurtosis(file3)
print("The kurtosis for data3 is", kurtosis3)
np.sort(counts3)
data1_ind3=np.unravel_index(np.argmax(counts3), counts3.shape)
print("The mode for data3 is", edges3[data1_ind3])
#T-test
s2 = []
s3 = []
for k in file2:
    f = np.power(np.absolute(np.subtract(np.average(file2), k)), 2)
    s2.append(f)
for l in file3:
    g = np.power(np.absolute(np.subtract(np.average(file3), l)), 2)
    s3.append(g)
ssquared = np.divide(np.add(np.sum(s2), np.sum(s3)), np.subtract(np.add(len(file2), len(file3)), 2))
t = np.divide(np.absolute(np.subtract(np.average(file2), np.average(file3))), np.power(np.add(np.divide(ssquared, len(file2)), np.divide(ssquared, len(file3))), 0.5))
print("This is the t value for data2 and data3", t)
print("Since t is less than 5, we can assume that the difference between the two data sets are not due to randomness.")

plt.show()
