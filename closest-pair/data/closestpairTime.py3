import sys
import fileinput
import math
import time
from operator import itemgetter

brutetime=0
striptime=0
stripbuildtime=0
ysorttime=0

def dist(p,q):
    return math.hypot(q[0]-p[0],q[1]-p[1])

def bruteForce(pointlist):
    ttime = time.time()
    mindist=sys.maxsize
    for i in pointlist:
        for j in pointlist[pointlist.index(i)+1:]:
            distance = dist(i,j)
            if distance < mindist:
                mindist=distance
    global brutetime
    brutetime+=time.time()-ttime
    return mindist

def stripClosest(ysorted, d):
    ttime = time.time()
    mind = d
    length = len(ysorted)
    n=0
    for p1 in ysorted:
        for p2 in ysorted[n+1:min(n+7, length)]:
            if p2[1]-p1[1]<mind:
                distance= dist(p1,p2)
                if distance<mind:
                    mind=distance
            else: 
                break
        n+=1
    global striptime
    striptime+=time.time()-ttime
    return mind


def closestPair(xsorted, ysorted,length):
    if length <= 3:
        return bruteForce(xsorted)
    midindex = length // 2
    xleft=xsorted[:midindex]
    xright=xsorted[midindex:]

    ttime=time.time()
    yleft  = sorted(xleft, key=itemgetter(1))
    yright = sorted(xright, key=itemgetter(1))
    global ysorttime
    ysorttime+=time.time()-ttime
    dl=closestPair(xleft,yleft, len(xleft))
    dr=closestPair(xright, yright, len(xright))
    d=min(dl,dr)
    mid = xright[0][0]
    ttime=time.time()
    strip = [x for x in ysorted if mid-d <= x[0] <= mid+d]
    global stripbuildtime
    stripbuildtime+=time.time()-ttime
    return min(d,stripClosest(strip, d))


ttime = time.time()
with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

names = {}
points=[]  # [[x1,y1, n], [x2,y2, m],...] where m and n are the points identifiers
n=0
for l in lines:
    line = l.split()
    if len(line)==3 and ':' not in line:
        names[n]=line[0]
        pointpair = list(map(float, line[1:]))
        points.append((pointpair[0],pointpair[1],n))
        n+=1
readTime=time.time()-ttime

xsorted = sorted(points, key=itemgetter(0))
ysorted = sorted(points, key=itemgetter(1))
length = len(xsorted)
print(closestPair(xsorted,ysorted,length))
print('Brute time: {} \nStrip time: {} \nStripbuild time: {} \nRead time: {} \nYsort time: {}'.format(brutetime,striptime,stripbuildtime, readTime,ysorttime))