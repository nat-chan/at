#!/bin/bash

file="$1"
workspaceFolder="$2"
fileDirname="$3"

# "./test/sample-1.in"から
#    test/sample-1 を抽出
sample=$(sed -n 's;^.*"\./\(.*\).in";\1;p' "${file}")

if [ -z "${sample}" ]; then
    sample="test/sample-1"
    echo "the specified sample number was not detected."
else
    echo "${sample} is detected."
fi

if [ -e "${fileDirname}/${sample}.in" -a -e "${fileDirname}/${sample}.out" ]; then
    cp "${fileDirname}/${sample}.in" "${workspaceFolder}/sample.in"
    cp "${fileDirname}/${sample}.out" "${workspaceFolder}/sample.out"
    echo "successfully copied ${sample}"
else
    echo "failed to copy ${sample}"
fi