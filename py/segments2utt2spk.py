#!/usr/bin/python3
import os
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")
import sys
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('segments',type=argparse.FileType('r'),default=sys.stdin)
parser.add_argument('utt2spk',type=argparse.FileType('w'),default=sys.stdout)
args=parser.parse_args()
for line in args.segments:
    parts=line.split()
    spkid1=parts[1]
    spkid=spkid1.split('_')[0]
    lbl=parts[0]
    args.utt2spk.write("{0}    {1}\n".format(lbl,spkid))
