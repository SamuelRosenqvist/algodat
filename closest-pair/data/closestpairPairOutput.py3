import sys
import fileinput
import math
from operator import itemgetter

def dist(p,q):
    return math.hypot(q[0]-p[0],q[1]-p[1])

def bruteForce(pointlist):
    mindist=sys.maxsize
    for i in pointlist:
        for j in pointlist[pointlist.index(i)+1:]:
            distance = dist(i,j)
            if distance < mindist:
                pair=(i,j)
                mindist=distance
    return (mindist,pair)

def stripClosest(ysorted, d, pair):
    mind = d
    length = len(ysorted)
    n=0
    for p1 in ysorted:
        for p2 in ysorted[n+1:min(n+7, length)]:
            if p2[1]-p1[1]<mind:
                distance= dist(p1,p2)
                if distance<mind:
                    pair=(p1,p2)
                    mind=distance
            else: 
                break
        n+=1
    return (mind,pair)


def closestPair(xsorted, ysorted,length):
    if length <= 3:
        return bruteForce(xsorted)
    midindex = length // 2
    xleft=xsorted[:midindex]
    xright=xsorted[midindex:]

    yleft  = sorted(xleft, key=itemgetter(1))
    yright = sorted(xright, key=itemgetter(1))
    dl,leftp=closestPair(xleft,yleft, len(xleft))
    dr,rightp=closestPair(xright, yright, len(xright))
    d=min(dl,dr)
    if dl < dr:
        pair = leftp
    else:
        pair = rightp
    mid = xright[0][0]
    strip = [x for x in ysorted if mid-d <= x[0] <= mid+d]
    ds,stripP=stripClosest(strip, d, pair)
    if ds < d:
        pair = stripP
    return (min(d,ds),pair)


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

xsorted = sorted(points, key=itemgetter(0))
ysorted = sorted(points, key=itemgetter(1))
length = len(xsorted)
dist, pair = closestPair(xsorted,ysorted,length)

if dist == 0:
    dist='0.0000000000000000'
print('{}: {} {}'.format(sys.argv[1], length, dist))
print('{} {}'.format(pair[0], pair[1]))