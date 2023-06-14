import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt 
x=[]
y=[]
z=[]
def findBH(s):
    iord=s.stars['iord']
    BHfilter = np.where(iord==60352780)
    BH = s.stars[BHfilter]
    return BH
def findBHpos(s):
    BH=findBH(s)
    BHpos=BH['pos']
    return BHpos
snapshots=np.loadtxt('p.list',dtype=np.str)
for i in range(len(snapshots)):
    s=pynbody.load(snapshots[i])
    s.physical_units()
    BHpos=findBHpos(s)
    print(BHpos)
    x.append(BHpos[0][0])
    y.append(BHpos[0][1])
    z.append(BHpos[0][2])