# -*- coding: utf-8 -*-
"""
Created on Wed May 12:25:48 2021

@author: Avanish @ pyMAINS
"""
import pandas as pd
from collections import Counter
import numpy as np
import os


'''
For reading dump files with header as follows 
----
ITEM: TIMESTEP
1000
ITEM: NUMBER OF ATOMS
28654560
ITEM: BOX BOUNDS pp pp pp
0 334.626 
0 339.032
266.978 3279.17
ITEM: ATOMS id type x y z vx vy vz c_2[1] c_2[2] c_2[3] c_3 c_4 
6555 1 49.8856 1.47846 269.395 -4.62697 -2.8043 10.9163 885723 -3.44425e+06 -1.72503e+06 21.6796 5 
------

Line 40 we skip 9 lines while reading through pandas as these are header
'''
filename='lammps_file.dump'

with open(filename) as myfile:
    head = [next(myfile) for x in range(9)]
ntime=int(float(head[1].split()[0]))
natom=int(float(head[3].split()[0]))
xmin,xmax= [float(i) for i in head[5].split()]
ymin,ymax= [float(i) for i in head[6].split()]
zmin,zmax= [float(i) for i in head[7].split()]

df=pd.read_csv(filename,sep='\s+',header=None,skiprows=9) #9 rows skipped based on the lammps dump file please confirm for your case
df.columns=head[8].split()[2:]

'''
For reading data files with header as follows 
----
#Data file created or converted using pyMAINS

  4000 atoms
	 2 atom types
0.00000000 36.14900000 xlo xhi
0.00000000 36.14900000 ylo yhi
0.00000000 36.14900000 zlo zhi

Masses

        1   55.84500000    # Fe
        2   63.54600000    # Cu

Atoms

1.0 2.0 0.0 0.0 0.0

------

Line 40 we skip 9 lines while reading through pandas as these are header
'''
filename='lammps_file.dump'

with open(filename) as myfile:
    head = [next(myfile) for x in range(16)]
ntime=int(float(head[1].split()[0]))
natom=int(float(head[3].split()[0]))
xmin,xmax= [float(i) for i in head[5].split()]
ymin,ymax= [float(i) for i in head[6].split()]
zmin,zmax= [float(i) for i in head[7].split()]

df=pd.read_csv(filename,sep='\s+',header=None,skiprows=9) #9 rows skipped based on the lammps dump file please confirm for your case
df.columns=head[8].split()[2:]






'''
Writing dump file
'''
with open('filename.dump', 'w') as f:
    f.write('ITEM: TIMESTEP\n')
    f.write('{}\n'.format(str(int(float(ntime)))))
    f.write('ITEM: NUMBER OF ATOMS\n')
    f.write('{}\n'.format(str(natom)))
    f.write('ITEM: BOX BOUNDS pp pp pp\n')
    f.write('{} {}\n'.format(str(xmin),str(xmax)))
    f.write('{} {}\n'.format(str(ymin),str(ymax)))
    f.write('{} {}\n'.format(str(zmin),str(zmax)))
    f.write('ITEM: ATOMS id type x y z vx vy vz c_2[1] c_2[2] c_2[3] c_3 c_4\n')  #Chnage the column name here           
df.to_csv('filename.dump',sep='\t',float_format=None,columns=twin_col,index=False,header=False,mode='a')
f.close()


'''
Writing data file
'''

with open('{}-Cu-fcc-{}-Fe.dat'.format(int(np.round((1-i)*100)),int(np.round(i*100))), 'w') as f:
    f.write('#Data file created or converted using pyMAINS\n')
    f.write('\n')
    f.write('  {} atoms\n'.format(str(C[2][0])))
    f.write('\t {} atom types\n'.format(str(cc.shape[0])))
    f.write('{} {} xlo xhi\n'.format(str(C[5][0]),str(C[5][1])))
    f.write('{} {} ylo yhi\n'.format(str(C[6][0]),str(C[6][1])))
    f.write('{} {} zlo zhi\n'.format(str(C[7][0]),str(C[7][1])))
    f.write('\n')
    f.write('Masses\n')
    f.write('\n')
    f.write('        1   55.84500000    # Fe\n')
    f.write('        2   63.54600000    # Cu\n')
    f.write('\n')
    f.write('Atoms\n')
    f.write('\n')
df.to_csv('{}-Cu-fcc-{}-Fe.dat'.format(int(np.round((1-i)*100)),int(np.round(i*100))),sep=' ',float_format=None,columns=['id','avani','x','y','z'],index=False,header=False,mode='a')

