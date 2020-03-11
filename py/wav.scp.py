# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:44:59 2020

@author: rahofa
"""
import os
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")

dest = "..\\data\\all\\wav.scp"
w=[]
train_file = "..\\data\\f_list\\wav_list.txt"
file_paths = open(train_file,'r')
for path in file_paths:
    path = path.strip()
    file_name=os.path.basename(path)
    print(file_name)
    split_filename=file_name.split('.')
    split_filename1=file_name.split('_')[0][4]
    #print(split_filename1)
    molecule_name=split_filename[0]
    picklefile =molecule_name+".wav"+".scp"
    folder=Path(path).parts
    w=(molecule_name+"    "+"/home/amal/newkaldi/kaldi/egs/spkrsim/data/wav/"+folder[3]+"/"+file_name)
    b='AR'
    if folder[3]==b:
        full_path = os.path.join(dest+"\\AR",picklefile)
        print(w, file=open(full_path, "a"))
    else:
        full_path1 = os.path.join(dest+"\\EN",picklefile)
        print(w, file=open(full_path1, "a"))

