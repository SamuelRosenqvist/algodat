import fileinput
import sys

infile1 = open(str(sys.argv[1]),'r')
infile2 = open(str(sys.argv[2]),'r')

correctcouples = []
couples = []
n=0
for line in fileinput.input():
    if fileinput.isfirstline():
        n+=1
    if n==1:
        correctcouples.append(line[:-1])
    if n==2:
        couples.append(line[:-1])

if len([c for c in correctcouples if c not in couples])==0:
    print(True)
else:
    print(False)
