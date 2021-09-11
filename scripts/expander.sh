#!/bin/bash
target_file=$(readlink -f $1)
target_dir=$(dirname $target_file)
root=$(dirname $0)/../
cd $root/ac-library/
expander.py $target_file
mv combined.cpp $target_dir