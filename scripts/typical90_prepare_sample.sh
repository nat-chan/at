#!/bin/bash

if [[ "${1}" = "--help" || -z "${1}" ]]; then
cat << EOF
Usage:
    $0 0XX

Description:
    0XX is a probrem number in typical90 contest (001~090)
EOF
exit
fi

id=${1}
mkdir -p "test"
n=1
wget -q https://raw.githubusercontent.com/E869120/kyopro_educational_90/main/sample/${id}.txt
cat ${id}.txt | nkf -w -Lu | sed -e '$a\\' \
    | while read line; do
        if [[ "${line}" = "# 入力例 ${n}" ]]; then
            echo -e "\x1b[32m[.in start]\x1b[m $line"
            file="test/sample-${n}.in"
            txt=""
        elif [[ "${line}" = "# 出力例 ${n}" ]]; then
            echo -e "\x1b[33m[.out start]\x1b[m $line"
            file="test/sample-${n}.out"
            txt=""
            ((n++))
        elif [[ "${line}" = "" && "${file}" != "" ]]; then
            echo -e "\x1b[31m[${file} saved]\x1b[m $line"
            echo -ne "${txt}" > "${file}"
            file=""
        else
            echo -e "\x1b[36m[concat txt]\x1b[m $line"
            txt+="${line}\n"
        fi
    done

wget -q https://raw.githubusercontent.com/E869120/kyopro_educational_90/main/problem-txt/${id}.txt
wget -q https://github.com/E869120/kyopro_educational_90/raw/main/problem/${id}.jpg