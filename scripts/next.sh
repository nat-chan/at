#!/bin/bash
pwd=$(basename $(pwd))
contest=${pwd:0:-2}
problem=${pwd: -1:1}
problem=$(echo $problem | tr "_a-z" "a-z_")
mkdir ../${contest}_${problem}/
cd ../${contest}_${problem}/
xdg-open https://atcoder.jp/contests/${contest}/tasks/${contest}_${problem}
oj-prepare https://atcoder.jp/contests/${contest}/tasks/${contest}_${problem}
code main.py

#cat << EOF | python /dev/stdin | while read url problem_id; do
#from selenium import webdriver
#options = webdriver.ChromeOptions()
#options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#driver = webdriver.Chrome(options=options)
#url = driver.current_url
#problem_id = url
#problem_id = problem_id.split("/")[-1]
#problem_id = problem_id.split("?")[0]
#print(url, problem_id)
#EOF
#cd $(dirname $0)/..
#mkdir $problem_id || exit 1
#cd $problem_id
#oj-prepare $url
#code main.py
#done
#