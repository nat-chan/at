#!/bin/bash
dir=$(readlink -f $(dirname $0))
${dir}/list_active_url.py|while read url; do
    url=$(echo "${url}"|tr -d '\r')
    if [ "${url}" = "None" ]; then
        exit 1
    fi
    echo "${url}"
    problem=$(basename "$url")
    cd "${dir}/.."
    mkdir "${problem}"
    cd "${problem}"
    oj-prepare "${url}"
    code main.py
    break
done