#!/bin/bash
data=$1
plotname=$2
out_File="$plotname_.png"
out_file="$plotname.png"

timeout 50m python3 Q2/q2_.py $data $plotname