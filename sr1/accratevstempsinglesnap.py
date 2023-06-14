import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt
import pynbody.plot.sph as sph
s=pynbody.load('/mnt/data0/jillian/h148/h148.cosmo50PLK.3072g3HbwK1BH.000139/h148.cosmo50PLK.3072g3HbwK1BH.000139')
s.physical_units()
def findBH(s):
    iord=s.stars['iord']
    BHfilter=np.where(iord==75288553)
    BH=s.stars[BHfilter]
    return BH
def findBHpos(s):
    BH=findBH(s)
    BHpos=BH['pos']
    return BHpos
BHpos=findBHpos(s)
print(BHpos)
radius='340 pc'
sphere=pynbody.filt.Sphere(radius,BHpos[0])
gas=s.gas[sphere]
temp=gas['temp']
su=sum(temp)
average=su/len(temp)
star=s.star[sphere]
iords=star['iord']
BHfilters=np.where(iords==101863565)
BHs=star[BHfilters]


