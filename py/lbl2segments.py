# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:44:54 2020

@author: rahofa
"""

import os
from pathlib import Path
import warnings
import numpy as np
warnings.filterwarnings("ignore")


def centiSecond(times):
    time=[]
    for p in range(len(times)):
        time.append(int(times[p][0]*100))
        time.append(int(times[p][1]*100)) 
    return time

dest = "..\\data\\segments"
w=[]
train_file = "C:\\users\\rahofa\\Python\\data\\f_list\\lbl_list.txt"
file_paths = open(train_file,'r')
for path in file_paths:
    path = path.strip()
    file_name=os.path.basename(path)
    print(file_name)
    split_filename=file_name.split('.')
    split_filename1=file_name.split('_')[0][4]
    #print(split_filename1)
    molecule_name=split_filename[0]
    #print(molecule_name)
    picklefile =molecule_name+".segment"+".txt"
    full_path = os.path.join(dest,picklefile)
    for pathlbl in path:
        times = []
        var=[]
        file = open(path, "r")
        for line in file:
            times.append([float(x) for x in line.strip().split( )[0:2]])
            var.append(line.strip().split( )[0:3])
            segemnt=centiSecond(times)
            segments=np.array(segemnt).reshape(-1, 2)
            folder=Path(path).parts
            #a=str(var)
    for p in range(len(times)):
        a=str(var[p][2])
        b=(segments[p][0])
        c=(segments[p][1])
        d=str(split_filename[0])
        e=str(times[p][0])
        f=str(times[p][1])
        w=(a+"_"+f'{b:06}'+"_"+f'{c:06}'+"    "+d+"    "+e+"    "+f)
        b='AR'
        if folder[3]==b:
            full_path = os.path.join(dest+"\\AR",picklefile)
            print(w, file=open(full_path, "a"))
        else:
            full_path1 = os.path.join(dest+"\\EN",picklefile)
            print(w, file=open(full_path1, "a"))
          
   # print("times:"+str(times))
    #print("index:"+str(index))
        file.close() 