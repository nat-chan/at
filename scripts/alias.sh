#!/bin/zsh

function pre(){
    id=$1
    arr=(${(s/_/)id})
    echo "contest: $arr[1]"
    echo "problem: $arr[2]"
    if [[ -z "$arr[1]" || -z "$arr[2]" ]]; then
        echo -e "\x1b[31mUsage: $0 abc001_a\x1b[m"
        return 1
    else
        mkdir -p ~/at/${id}
        cd ~/at/${id}
        if [[ -z "$(ls -a ~/at/${id})" ]]; then
            url="https://atcoder.jp/contests/${arr[1]}/tasks/${id}"
            xdg-open "${url}"
            oj-prepare "${url}"
            code main.py
        else
            echo -e "\x1b[31m~/at/${id} is not empty\x1b[m"
            return 1
        fi
    fi
}
