#!/bin/bash
data=$1
plotname=$2
out_File="$plotname_.png"
out_file="$plotname.png"

python3 Q1/preprocessing.py $data gspan
python3 Q1/preprocessing.py $data fsg
python3 Q1/preprocessing.py $data gaston
timeout 40m python3 Q1/q1.py $data $plotname
if ! [[ -f $out_File ]]
then
	python3 Q1/q1_alt.py $plotname
fi
#python3 Q1/q1_alt.py $plotname