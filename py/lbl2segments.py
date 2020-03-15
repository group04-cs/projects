#!/usr/bin/python3
import os
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")
import sys
import argparse 
parser = argparse.ArgumentParser()
parser.add_argument('lbllist',type=argparse.FileType('r'),default=sys.stdin)
parser.add_argument('segments',type=argparse.FileType('w'),default=sys.stdout)
args=parser.parse_args()
for path in args.lbllist:
    path = path.strip()
    file_name=os.path.basename(path)
    split_filename=file_name.split('.')
    molecule_name=split_filename[0]
    with open(path, 'r') as lblfile:
        for line in lblfile:
            parts=line.split();
            lbl=parts[2]
            wavid=molecule_name
            sttime= float(parts[0])
            entime= float(parts[1])
            sttimec=int(sttime*100)
            entimec=int(entime*100)
            args.segments.write("{0}_{1:06}_{2:06}    {3}    {4}    {5}\n".format(lbl,sttimec,entimec,wavid,sttime,entime))
