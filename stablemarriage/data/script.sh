for FILE in *-in.txt

do
	echo $FILE
	base=${FILE%-in.txt}
    python stablemarriage.py3 < $FILE > $base.sa7638ros.out.txt # replace with your command!
    python checkdif.py3 $base-out.txt $base.sa7638ros.out.txt
done
