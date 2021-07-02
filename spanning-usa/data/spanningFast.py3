import fileinput
import sys
import re
import time
import heapq

with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

class Disjoint:

    def __init__(self):
        self.sets = []
        self.parentpointers = {}
        self.t=0

    def createSet(self, repr):
        self.sets.append([repr])
        self.t+=1
        self.parentpointers[repr]=self.t

    def mergeSets(self, set1, set2):
        if set1 != set2:
            parent = self.parentpointers[set1[0]]
            for s in set2:
                self.parentpointers[s]=parent
            set1.extend(set2)
            self.sets.remove(set2)
    
    def findSet(self, repr1):
        for oneSet in self.sets:
            if repr1 in oneSet:
                return oneSet
    
    def unionFind(self, repr1, repr2):
        if self.parentpointers[repr1]==self.parentpointers[repr2]:
            return True
        else:
            return False
            
readtime=time.time()
citygraph=[]
edges = []
T = Disjoint()
for c in lines:
    if('--' not in c):
        T.createSet(int(c))
    else:
        names  = c.split(" ")
        length = int(names[-1][1:-1])
        name1,name2 = names[0].split('--')
        edges.append((length,int(name1),int(name2)))
        
print("Readtime is: %s" %(time.time()-readtime))

A=[]
edges = sorted(edges)
nedges= len(edges)
nverts= len(citygraph)

algtime=time.time()
for e in edges:         # Kruskal's
    if nedges==nverts-1:
        break
    if not T.unionFind(e[1],e[2]):
        A.append(e)
        T.mergeSets(T.findSet(e[1]),T.findSet(e[2]))
print("Kruskal's time is: %s" %(time.time()-algtime))
t=0
for a in A:
    t+=a[0]
print(t)