import sys
import fileinput
import math
import time
from operator import itemgetter

def findMin(pointlist):
    findmintime=time.time()
    mindist=sys.maxsize
    for i in pointlist:
        for j in pointlist[pointlist.index(i)+1:]:
            dist = math.hypot(j[0]-i[0], j[1]-i[1])
            if dist < mindist:
                mindist=dist
                global minPair
                minPair=(i,j)
    print("Findmintime: %f" %(time.time()-findmintime))
    return mindist

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

minPair=()
names = {}
points=[]  # [[x1,y1, n], [x2,y2, m],...] where m and n are the points identifiers
n=0
readtime=time.time()
for l in lines:
    line = l.split()
    if len(line)==3 and ':' not in line:
        names[n]=line[0]
        pointpair = list(map(float, line[1:]))
        pointpair.append(n)
        points.append(pointpair)
        n+=1
print("Readtime: %f" %(time.time()-readtime))

if len(points)<4:
    print(findMin(points))
    # print('{} -- {}'.format(names[minPair[0][2]], names[minPair[1][2]]))
    sys.exit(0)
    
sorttime=time.time()
points.sort()
print("Sorttime: %f" %(time.time()-sorttime))
xright=points[int(len(points)/2):]
xleft=points[:int(len(points)/2)]

minD  = min(findMin(xleft),findMin(xright))
mid = xright[0][0]

strip  = []
xbound = mid + minD
for p in xright:
    if p[0] < xbound:
        strip.append(p)
    else: 
        break

xbound = mid - minD
for p in xleft:
    if p[0] > xbound:
        strip.append(p)
    else: 
        break

ysorted = sorted(strip, key=itemgetter(1))
stripmintime=time.time()
for p1 in strip:
    for p2 in strip[strip.index(p1)+1:]:
        if p2[1]-p1[1]<minD:
            continue
        elif math.hypot(p2[0]-p1[0], p2[1]-p1[1])<minD:
            minD=math.hypot(p2[0]-p1[0], p2[1]-p1[1])
            minPair=(p1,p2)
print("Stripmintime: %f" %(time.time()-stripmintime))
print(minD)
# print('{} -- {}'.format(names[minPair[0][2]], names[minPair[1][2]]))