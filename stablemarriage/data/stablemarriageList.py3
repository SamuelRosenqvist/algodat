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
        femaleList[person//2-1][1].extend(invertedPreflist)
    elif person%2!=0:
        maleList[(person-1)//2][1].extend(prefList)

def readFile(infile):
    maleList   = [] # format of elements: tuple (nr name, [preference list])
    femaleList = [] # position in list nr, 2*pos+1, femaleList 2n
    n          = 1
    t          = 0

    infile = open(str(infile),'r')

    # read input and put into data structures
    for line in fileinput.input(): #infile:  #in sys.stdin:
        lineList = line.split()
        lineHead=line[0]
        if lineHead[0]== '#' or lineHead== '\n':
            pass
        elif lineList[0][-1:]==':':
            prefs = lineList[1:]
            insPref(lineList[0][:-1], prefs, n)
            t+=1
            if t>=n*2:
                break
        elif lineHead[0]=='n':
            n=int(lineList[0][2:])
        elif int(lineList[0])%2==0:
            femaleList.append((line[:-1],[]))
        elif int(lineList[0])%2!=0:
            maleList.append((line[:-1],[]))

    #Gale-Shapley algorithm
    couples = []
    while maleList != []:
        male =   maleList.pop(0)
        female = femaleList[int(male[1].pop(0))//2-1]
        pair = [item for item in couples if female in item]
        if not pair:
            couples.append((male,female))
        else:
            femprefList = female[1]
            engagedMale = pair[0][0]
            if femprefList[(int(male[0].split()[0])-1)//2] < femprefList[(int(engagedMale[0].split()[0])-1)//2]:
                couples.remove(pair[0])
                couples.append((male,female))
                maleList.append(engagedMale)
            else:
                maleList.append(male)

    strlist =[]
    #print result
    for p in couples:
        strlist.append(p[0][0].split()[1] + " -- " + p[1][0].split()[1])
    return strlist
