import sys
import fileinput
import itertools

mismatchindex=['A','R','N','D','C','Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V','B','Z','X','*']
mismatch={}  # A  R  N  D  C  Q  E  G  H  I  L  K  M  F  P  S  T  W  Y  V  B  Z  X  *
mismatch['A'] =  "4 -1 -2 -2  0 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -3 -2  0 -2 -1  0 -4"
mismatch['R'] =  "-1  5  0 -2 -3  1  0 -2  0 -3 -2  2 -1 -3 -2 -1 -1 -3 -2 -3 -1  0 -1 -4"
mismatch['N'] =  "-2  0  6  1 -3  0  0  0  1 -3 -3  0 -2 -3 -2  1  0 -4 -2 -3  3  0 -1 -4"
mismatch['D'] =  "-2 -2  1  6 -3  0  2 -1 -1 -3 -4 -1 -3 -3 -1  0 -1 -4 -3 -3  4  1 -1 -4"
mismatch['C'] =  "0 -3 -3 -3  9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1 -3 -3 -2 -4"
mismatch['Q'] =  "-1  1  0  0 -3  5  2 -2  0 -3 -2  1  0 -3 -1  0 -1 -2 -1 -2  0  3 -1 -4"
mismatch['E'] =  "-1  0  0  2 -4  2  5 -2  0 -3 -3  1 -2 -3 -1  0 -1 -3 -2 -2  1  4 -1 -4"
mismatch['G'] =  "0 -2  0 -1 -3 -2 -2  6 -2 -4 -4 -2 -3 -3 -2  0 -2 -2 -3 -3 -1 -2 -1 -4"
mismatch['H'] =  "-2  0  1 -1 -3  0  0 -2  8 -3 -3 -1 -2 -1 -2 -1 -2 -2  2 -3  0  0 -1 -4"
mismatch['I'] =  "1 -3 -3 -3 -1 -3 -3 -4 -3  4  2 -3  1  0 -3 -2 -1 -3 -1  3 -3 -3 -1 -4"
mismatch['L'] =  "-1 -2 -3 -4 -1 -2 -3 -4 -3  2  4 -2  2  0 -3 -2 -1 -2 -1  1 -4 -3 -1 -4" 
mismatch['K'] =  "-1  2  0 -1 -3  1  1 -2 -1 -3 -2  5 -1 -3 -1  0 -1 -3 -2 -2  0  1 -1 -4" 
mismatch['M'] =  "-1 -1 -2 -3 -1  0 -2 -3 -2  1  2 -1  5  0 -2 -1 -1 -1 -1  1 -3 -1 -1 -4" 
mismatch['F'] =  "-2 -3 -3 -3 -2 -3 -3 -3 -1  0  0 -3  0  6 -4 -2 -2  1  3 -1 -3 -3 -1 -4" 
mismatch['P'] =  "-1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4  7 -1 -1 -4 -3 -2 -2 -1 -2 -4" 
mismatch['S'] =  " 1 -1  1  0 -1  0  0  0 -1 -2 -2  0 -1 -2 -1  4  1 -3 -2 -2  0  0  0 -4" 
mismatch['T'] =  " 0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1  1  5 -2 -2  0 -1 -1  0 -4" 
mismatch['W'] =  "-3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1  1 -4 -3 -2 11  2 -3 -4 -3 -2 -4" 
mismatch['Y'] =  "-2 -2 -2 -3 -2 -1 -2 -3  2 -1 -1 -2 -1  3 -3 -2 -2  2  7 -1 -3 -2 -1 -4" 
mismatch['V'] =  " 0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4 -3 -2 -1 -4" 
mismatch['B'] =  "-2 -1  3  4 -3  0  1 -1  0 -3 -4  0 -3 -3 -2  0 -1 -4 -3 -3  4  1 -1 -4" 
mismatch['Z'] =  "-1  0  0  1 -3  3  4 -2  0 -3 -3  1 -1 -3 -1  0 -1 -3 -2 -2  1  4 -1 -4" 
mismatch['X'] =  " 0 -1 -1 -1 -2 -1 -1 -1 -1 -1 -1 -1 -1 -1 -2  0  0 -2 -1 -1 -1 -1 -1 -4" 
mismatch['*'] =  "-4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4 -4  1" 
for x in mismatch:
    mismatch[x] = list(map(int, mismatch[x].split()))

def find(f, seq):
    for item in seq:
        if f(item):
            return item

def mismatchNo(x,y):
    return mismatch[x][mismatchindex.index(y)]

def Alignment(X,Y):
    delta=-4
    m=len(X)+1
    n=len(Y)+1
    A=[0]*m
    tracebackm=[0]*m
    for i in range(0,m):
        A[i]=[0]*n
        tracebackm[i]=[0]*n
    for t in range(0,n):
        A[0][t]=t*delta
        tracebackm[0][t]=(0,-1)
    for t in range(0,m):
        A[t][0]=t*delta
        tracebackm[t][0]=(-1,0)
    tracebackm[0][0]=(0,0)

    for j in range(1,n):
        for i in range(1,m):
            x=X[i-1]
            y=Y[j-1]
            cost1 = mismatchNo(x,y)+A[i-1][j-1]
            cost2 = delta + A[i-1][j]
            cost3 = delta + A[i][j-1]
            best=max(cost1,cost2,cost3)
            A[i][j]=best
            path=()
            if best==cost1:
                path=(-1,-1)
            if best==cost2:
                path=(-1,0)
            if best==cost3:
                path=(0,-1)
            tracebackm[i][j]=path
    w1=list(X)
    w2=list(Y)
    s1=''
    s2=''
    p,q=tracebackm[-1][-1]
    i,j=m-1,n-1
    while (i,j)!=(0,0):
        if not w2:
            w2.append('-')
        if not w1:
            w1.append('-')
        if (p,q)==(-1,-1):
            s1=w1.pop()+s1
            s2=w2.pop()+s2
        elif (p,q)==(-1,0):
            s1=w1.pop()+s1
            s2='-'+s2
        elif (p,q)==(0,-1):
            s1='-'+s1
            s2=w2.pop()+s2
        i+=p
        j+=q
        (p,q)=tracebackm[i][j] 
    return (s1,s2, A[-1][-1])


with open(sys.argv[1]) as f:
    lines = f.read().splitlines()

genomest = []
t=1
q=[]
lines=lines[1:]
for l in lines:
    if len(l.split())==2:
        q.append(l.split())
    else:
        if t%2!=0:
            genomest.append((l,[]))
        else: 
            genomest[-1][1].append(l)
        t+=1

genomes=[]
for x in genomest:
    genomes.append((x[0],[y for t in x[1] for y in t]))
alignments=[]
for pair in q:
    x=[item for item in genomest if item[0]==pair[0]]
    y=[item for item in genomest if item[0]==pair[1]]
    alignments.append((pair[0],pair[1],Alignment(x[0][1][0],y[0][1][0])))

for a in alignments:
    print("{}--{}: {}".format(a[0],a[1],a[2][2]))
    #print("{}\n{}".format(a[2][0],a[2][1]))