#!/bin/sh
for FILE in `ls -rS *-test.in`
do
	echo $FILE
	base=${FILE%-test.in} #create a new variable 'base' for without the -in.txt ending
    python word-ladders.py3 $base.dat $FILE > $base.sa7638ros.out # replace with your command and output to your own file
    diff $base.sa7638ros.out $base-test.out
done