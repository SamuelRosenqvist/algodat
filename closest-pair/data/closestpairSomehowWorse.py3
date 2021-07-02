import sys
import fileinput
import math
from operator import itemgetter

def dist(p,q):
    return math.hypot(q[0]-p[0],q[1]-p[1])

def bruteForce(px):
    p1,p2=px[0],px[1]
    min = dist(p1,p2)
    pxlen = len(px)
    if pxlen == 2:
        return p1,p2,min
    for i in range(pxlen-1):
        for j in range(i+1,pxlen):
            if i!=0 and j!=0:
                d = dist(px[i],px[j])
                if d < min:
                    min = d
                    p1, p2 = px[i],px[j]
    return p1,p2,min

def stripClosest(sx, sy, d, pair):
    striplnx=len(sx)
    midx = sx[striplnx//2][0]

    strip = [p for p in sy if midx - d <= p[0] <= midx + d]

    delta = d
    striplny=len(strip)

    for i in range(striplny-1):
        for j in range(i+1, min(i+7, striplny)):
            p,q = strip[i], strip[j]
            distance = dist(p,q)
            if distance < delta:
                pair = p,q
                delta = distance
    return pair[0], pair[1], delta


def closestPair(px,py):
    pxlen = len(px)
    if pxlen <= 3:
        return bruteForce(px)
    mid = pxlen//2
    Lx = px[:mid]
    Rx = px[mid:]

    midx = px[mid][0]
    Ly = list()
    Ry = list()
    for x in py:
        if x[0] <= midx:
            Ly.append(x)
        else:
            Ry.append(x)
    (L1,R1,min1) = closestPair(Lx, Ly)
    (L2,R2,min2) = closestPair(Rx, Ry)

    if min1 <= min2:
        d = min1
        mn = (L1,R1)
    else:
        d = min2
        mn = (L2,R2)
    
    (L3,R3,min3) = stripClosest(px,py, d, mn)

    if d <= min3:
        return mn[0], mn[1], d
    else:
        return L3, R3, min3


with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

minPair=()
names = {}
points=[]  # [[x1,y1, n], [x2,y2, m],...] where m and n are the points identifiers
n=0
for l in lines:
    line = l.split()
    if len(line)==3 and ':' not in line:
        names[n]=line[0]
        pointpair = list(map(float, line[1:]))
        pointpair.append(n)
        points.append(pointpair)
        n+=1

px = sorted(points, key=lambda x: x[0])
py = sorted(points, key=lambda x: x[1])
print(closestPair(px,py)[2])