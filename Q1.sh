#!/bin/bash
data=$1
plotname=$2
out_file="$plotname.png"

python3 Q1/preprocessing.py $data gspan
python3 Q1/preprocessing.py $data fsg
python3 Q1/preprocessing.py $data gaston
timeout 40m python3 Q1/q1.py $data $plotname
python3 Q1/q1_alt.py $plotname
