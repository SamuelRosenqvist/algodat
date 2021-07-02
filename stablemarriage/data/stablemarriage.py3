import fileinput
import sys
import operator

#inserts preference list
def insPref(person, prefList, n):
    person = int(person)
    if person%2==0:
        temp=1
        invertedPreflist=[None]*(n)
        for pref in prefList:
            invertedPreflist[(int(pref)-1)//2]=temp
            temp+=1
        femaleDict[person]=invertedPreflist
    elif person%2!=0:
        maleList.append((person, prefList))

maleList    = [] # elements: (nr, [preference list])
femaleDict  = {} # key nr -> value inverted preflist
names       = [] # names on index n-1
n          = 1
t          = 0

# read input and put into data structures
for line in sys.stdin:
    lineList = line.split()
    if not line.strip() or lineList[0][0]== '#':
        pass
    elif lineList[0][-1:]==':':
        prefs = lineList[1:]
        insPref(lineList[0][:-1], prefs, n)
        t+=1
        if t>=n*2:
            break
    elif lineList[0][0]=='n':
        n=int(lineList[0][2:])
    else:
        names.append(lineList[1])

#Gale-Shapley algorithm
couples = {} # key female(nr) -> value male(tuple)
while maleList != []:
    male =   maleList.pop(0)
    female = int(male[1].pop(0))
    if female not in couples:
        couples[female]=male
    else:
        femprefList = femaleDict[female]
        engagedMale = couples[female]
        if femprefList[(male[0]-1)//2] < femprefList[(engagedMale[0]-1)//2]:
            couples[female]=male
            maleList.append(engagedMale)
        else:
            maleList.append(male)

#print result
for key in couples:
    print(names[couples[key][0]-1] +" -- "+ names[key-1])
