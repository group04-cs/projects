#!/usr/bin/python3
import os
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")
import sys
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('wavlist',type=argparse.FileType('r'),default=sys.stdin)
parser.add_argument('wavscp',type=argparse.FileType('w'),default=sys.stdout)
args=parser.parse_args()
for path in args.wavlist:
    path = path.strip()
    file_name=os.path.basename(path)
    split_filename=file_name.split('.')
    molecule_name=split_filename[0]
    folder=Path(path).parts
    w=("/home/amal/newkaldi/kaldi/egs/spkrsim/import/wav/"+folder[3]+"/"+file_name)
    args.wavscp.write("{0}    {1}\n".format(molecule_name,w))
