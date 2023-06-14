import os, sys, pickle
import numpy as np
import pynbody
import matplotlib.pyplot as plt
import pynbody.plot.sph as sph
snapshots=np.loadtxt('sandrasnapshot.list',dtype=np.str)
for i in range(len(snapshots)):
    s=pynbody.load(snapshots[i])
    s.physical_units()
    def findBH(s):
        iord=s.stars['iord']
        BHfilter=np.where(iord==101863565)
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
    pynbody.analysis.angmom.faceon(gas)
    sph.image(gas,qty='temp',width=2,denoise=True,approximate_fast=False)
    plt.savefig("gassphere"+str([i])+".png")
plt.show()
