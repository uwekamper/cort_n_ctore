#!/bin/sh

FILE=$1
PROJECT=$2


echo $PROJECT
source ${PROJECT}/bin/activate

coffee -m -c $FILE.coffee
mv $FILE.map $FILE.js.map
sed -e s/sourceMappingURL="$FILE".map/sourceMappingURL="$FILE".js.map/ $FILE.js > $FILE.js.tmp
rm $FILE.js
mv $FILE.js.tmp $FILE.js
