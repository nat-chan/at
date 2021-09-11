#!/bin/bash
url=$1
curl -L "$url" > download.zip
unzip download.zip
mkdir dropbox
for f in in/* ; do
    mv $f ${f%.txt}.in
done
for f in out/* ; do
    mv $f ${f%.txt}.out
done
mv in/* dropbox
mv out/* dropbox
rm download.zip
rmdir in
rmdir out