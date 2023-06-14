import pickle
import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits import mplot3d
#MY MASS ACCRETION RELATION JUST A SUBPLOT OF PERCENTAGE OF MASS ACRRETED VS TOTAL MASS FOR ALL BLACK HOLES IN RUTH AND SANDRA.
file="orbits.pkl"
with open(file,'rb') as f:
    data=pickle.load(f)
yay=data['data']
file2='acclog.pkl'
with open(file2,'rb') as f:
    data2=pickle.load(f)
yay2=data2['data']
mass=[]
ratio=[]
for i in range(len(yay)):
    yay[i]['mass'][-1]
    if yay[i]['mass'][-1]>0:
        mass.append(yay[i]['mass'][-1])
        
for j in range(len(yay2)):
    Mgas=yay2[j]['deltaMgas']
    cuMgas=np.cumsum(Mgas)[-1]
    Mbh=yay2[j]['Mbh'][-1]
    ratio2=cuMgas/Mbh
    if yay2[j]['Mbh'][-1]>0:
        ratio.append(ratio2)

file3="sandra.orbits.pkl"
with open(file3,'rb') as f:
    data=pickle.load(f)
yay3=data['data']
file4='sandra.acclog.pkl'
with open(file4,'rb') as f:
    data4=pickle.load(f)
yay4=data4['data']
for k in range(len(yay3)):
    yay3[k]['mass'][-1]
    if yay3[k]['mass'][-1]>0:
        mass.append(yay3[k]['mass'][-1])
        
for l in range(len(yay4)):
    Mgas=yay4[l]['deltaMgas']
    cuMgas=np.cumsum(Mgas)[-1]
    Mbh=yay4[l]['Mbh'][-1]
    ratio4=cuMgas/Mbh
    if yay4[l]['Mbh'][-1]>0:
        ratio.append(ratio4)
        
nratio=[m*100 for m in ratio]    
plt.scatter(np.log10(mass),nratio,s=25)
plt.ylabel('Accretion percentage at z=0',fontsize=20)
plt.xlabel('Log Final Mass ($M_{\odot}$)',fontsize=20)
plt.title('Accretion Percentage vs Total Mass at z=0',fontsize=25)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()