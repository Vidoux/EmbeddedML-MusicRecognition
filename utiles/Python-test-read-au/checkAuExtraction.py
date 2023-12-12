# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 22:26:59 2021

@author: Louis
"""
import numpy as np
import pandas as pd

file_au='../Audio/blues.00000.au'
file_c='signal.csv'
Fe=22050

def readAuFile(file):
    with open(file, 'rb') as au:
        magic_number = au.read(4)
        print("Magical number: Ox%x" % int.from_bytes(magic_number, byteorder='big'))
        dataoffset = int.from_bytes(au.read(4), byteorder='big', signed=True)
        print("Data offset: %d" % dataoffset)
        datasize = int.from_bytes(au.read(4), byteorder='big', signed=True)
        print("Data size: %d" % datasize)
        au.seek(0)
        au.read(dataoffset)  
        data = au.read(datasize)
            
    d = []
    for i in range(0, datasize, 2): 
        d.append(int.from_bytes(data[i:i + 2], byteorder='big', signed=True))
    d=np.asarray(d, dtype=np.int16)
    return d

d1=readAuFile(file_au)
d2=pd.read_csv(file_c, header=None)
d2=d2.to_numpy()
d2=d2.reshape((d2.shape[1],))

if np.array_equal(d1, d2):
    print('Extraction is Okay !')
else:
   print('There is error during extraction')     