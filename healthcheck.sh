#!/bin/bash

for dirname in abc*_* arc*_*; do
    cd ${dirname}
        if [ -e ./main ]; then
            cmd="./main"
        else
            cmd="python main.py"
        fi
        arr=($(oj t --tle 4 -c "${cmd}" 2>/dev/null|tail -3|xargs))
        sec=${arr[2]}
        mem=${arr[9]}
        status=${arr[13]}
        ac=${arr[16]}
        all=${arr[19]}
        if [ "${status}" = "[SUCCESS]" ]; then
            dirname="\033[32m${dirname}\033[m"
            all="${ac}"
        else
            dirname="\033[31m${dirname}\033[m"
        fi
        echo -e "${dirname} ${sec}[sec] ${mem}[MB] ${ac}/${all} \"${cmd}\""
    cd ..
done