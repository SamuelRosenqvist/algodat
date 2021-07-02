import fileinput
import sys
import re

datafile = open(sys.argv[1])

class Disjoint:

    def __init__(self):
        self.sets = []

    def createSet(self, repr):
        self.sets.append([repr])

    def mergeSets(self, repr1, repr2):
        set1 = self.findSet(repr1)
        set2 = self.findSet(repr2)
        if set1 != set2:
            set1.extend(set2)
            self.sets.remove(set2)
    
    def findSet(self, repr1):
        for oneSet in self.sets:
            if repr1 in oneSet:
                return oneSet

class city:

    def __init__(self,name):
        self.name = name

def find(f, seq):
    for item in seq:
        if f(item):
            return item

inlist = datafile.read().splitlines()
citygraph=[]
index = next(i for i, v in enumerate(inlist) if '--' in v)
edges = []
unsortedi = 0
t=1
for c in inlist:
    if(t<=index):
        cname = re.sub('"','',c)
        citygraph.append(city(cname))
        t+=1
    else:
        length = int(c.split(" ")[-1][1:-1])
        names  = c[:-1-int(len(c.split("--")[1].split(" ")[-1]))]
        name1,name2 = list(map(lambda x: re.sub('"','',x), names.split("--")))
        city1 = find(lambda name: re.sub(' ','',name.name) == re.sub(' ','',name1),citygraph)
        city2 = find(lambda name: re.sub(' ','',name.name) == re.sub(' ','',name2),citygraph)
        edges.append((length,unsortedi,city1,city2))
        unsortedi+=1

T = Disjoint()
edges = sorted(edges)
A=[]
for v in citygraph:
    T.createSet(v)
for e in edges:         # Kruskal's
    set1 = T.findSet(e[2])[0]
    set2 = T.findSet(e[3])[0]
    if set1 != set2:
        A.append(e)
        T.mergeSets(set1,set2)

t=0
for a in A:
    print(a[0])
    print(a[2].name)
    print(a[3].name)
    t+=a[0]
print(t)