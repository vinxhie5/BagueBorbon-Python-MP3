import numpy as np
import ast

ns = input('Enter the data point/s in the form [x,y],[x,y],...:  ') 

nl = ast.literal_eval(ns) 
n = np.asarray(nl) 
print (n)

for i in range(len(n)):
    pf = np.polyfit(n[:,0], n[:,1],i)
    pv = np.polyval(pf, n[:,0])
    la = np.linalg.norm(n[:,1] - pv)
    a = [i,la]

    if i==0:
        x = a
    elif x[1] >= a[1]:
        y = a[0]
            
pf = np.polyfit(n[:,0],n[:,1],y)
print('The coefficients are: ',pf)
    
