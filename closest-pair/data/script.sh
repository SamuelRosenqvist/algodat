for FILE in *.tsp

do
	echo $FILE
	base=${FILE%.tsp}
    python closestpair.py3 $FILE
done
