#!/bin/bash

while [ $(date +%H) -ne 21 ]; do
    date
    sleep 1
done

sleep 1

i=a
mkdir ${1}_${i}
cd ${1}_${i}
oj-prepare https://atcoder.jp/contests/${1}/tasks/${1}_${i}
xdg-open https://atcoder.jp/contests/${1}/tasks/${1}_${i}
code main.py
