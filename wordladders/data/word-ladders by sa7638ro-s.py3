import fileinput
import sys

class word:
    
    def __init__(self,s):
        self.s = s
        self.last4=''.join(sorted(s[-4:]))
        self.sortedS=''.join(sorted(self.s))
        self.verts=set()
        self.p = False
        self.prev = -1
        self.length= 0
    
    def reset(self):
        self.p      = False
        self.prev   = -1
        self.length =  0

    def addVertex(self, w):
        self.verts.add(w)
    
    def getVerts(self):
        return self.verts

    def getFlag(self):
        return self.p

    def getPrev(self):
        return self.prev

    def getLength(self):
        return self.length

    def setFlag(self, p):
        self.p = p
    
    def setPrev(self, prev):
        self.prev = prev

    def setLength(self,length):
        self.length=length

def shortest_path(graph,start,target): #bfs
    changed=[]
    queue=[]
    start.setFlag(True)
    queue.append(start)
    changed.append(start)
    while queue:
        vertex = queue.pop(0)
        if vertex==target:
            length = vertex.getLength()
            for c in changed:
                c.reset()
            return length
        for w in vertex.getVerts():
            if not w.getFlag():
                w.setFlag(True)
                w.setPrev(vertex)
                w.setLength(vertex.getLength()+1)
                queue.append(w)
                changed.append(w)


def find(f, seq):
    for item in seq:
        if f(item):
            return item

datafile = open(sys.argv[1])
infile   = open(sys.argv[2])

wordlist = datafile.read().splitlines()
wordpairs = infile.read().splitlines()
sortedList = []

for w in wordlist: #creates list from words, creates word objects 
    sortedList.append(word(w))

sortedList = sorted(sortedList, key=lambda word: word.sortedS) #sorts list list alphabetically

#build the graph by connecting words
for w in sortedList:
    last4 = w.last4 #word looking for vertices
    for xw in sortedList:
        if(w!=xw):
            xws = xw.sortedS
            if((last4[0]==xws[0]) or (last4[0]==xws[1])):
                wlist = sorted(last4)
                xlist = sorted(xws)
                for c in wlist:
                    try:
                        xlist.remove(c)
                    except ValueError:
                        continue
                if(len(xlist)==1):
                    w.addVertex(xw)

#computing length using bfs
lengthList = []
for sp in wordpairs:
    sw, tw = sp.split()
    if(sw==tw):
        lengthList.append(0)
    else:
        startw = find(lambda word: word.s == sw, sortedList)
        targetw= find(lambda word: word.s == tw, sortedList)
        wverts = startw.getVerts()
        
        if(not wverts):
            lengthList.append(-1)
        else:
            length = shortest_path(sortedList,startw,targetw)
            if length:
                lengthList.append(length)
            else:
                lengthList.append(-1)

for i in lengthList:
    print(i)