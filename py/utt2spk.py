# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:44:56 2020

@author: rahofa
"""

import os
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")


dest = "..\\data\\utt2spk"
w=[]
train_file = "..\\data\\f_list\\segments_list.txt"
file_paths = open(train_file,'r')
for path in file_paths:
    path = path.strip()
    file_name=os.path.basename(path)
    print(file_name)
    split_filename=file_name.split('.')
    split_filename1=file_name.split('_')
    #print(split_filename1)
    molecule_name=split_filename1[0]
    #print(molecule_name)
    picklefile =molecule_name+".utt2spk"+".txt"
    full_path = os.path.join(dest,picklefile)
    for pathlbl in path:
        var=[]
        file = open(path, "r")
        for line in file:
            var.append(line.strip().split( )[0:3])
            folder=Path(path).parts
            #print(var[0][0])
    for p in range(len(var)):
        a=str(var[p][0])
        w=(a+"    "+molecule_name)
        b='AR'
        if folder[3]==b:
            full_path = os.path.join(dest+"\\AR",picklefile)
            print(w, file=open(full_path, "a"))
        else:
            full_path1 = os.path.join(dest+"\\EN",picklefile)
            print(w, file=open(full_path1, "a"))
        file.close()