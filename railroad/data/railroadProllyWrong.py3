import sys
import itertools

def dfs(C, F, s, t):
        visited=[]
        stack = [s]
        paths={s:[]}
        if s == t:
                return paths[s]
        while(stack):
                u = stack.pop()
                for v in range(len(C)):
                        if C[u][v]==-1 or (C[u][v]-F[u][v]>0) and v not in paths:
                                paths[v] = paths[u]+[(u,v)]
                                #print (paths)
                                global cut
                                cut.append((u,v))
                                if v == t:
                                        #print(paths[v])
                                        return paths[v]
                                stack.append(v)
                visited.append(u)
        global s_cut
        s_cut=set(visited)
        return None

def ford_fulkerson(C, s, t):
        if s==t:
                return 0
        n = len(C) # C is the capacity matrix
        F = [[0] * n for i in range(n)] # F is a matrix for current flow
        path = dfs(C, F, s, t)
        while path != None:
                #print("{} {} {}".format(s,t,len(path)))
                flow=sys.maxsize
                for u,v in path:
                        if C[u][v]!=-1:
                                temp= C[u][v] - F[u][v]
                                flow=min(flow, temp)
                        else: 
                                temp= sys.maxsize - F[u][v]
                                flow=min(flow, temp)
                for u,v in path:
                        F[u][v] += flow
                        F[v][u] -= flow
                #print("sum {}".format(sum(F[s][i] for i in range(n))))
                path = dfs(C,F,s,t)
        return sum(F[s][i] for i in range(n))


with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

n=int(lines[0])
m=int(lines[n+1])
nodes=[]
s_cut=[]
cut=[]
for l in lines[1:n+1]:
        nodes.append(l)

capacity_matrix=[[0]*n for i in range(n)]

for l in lines[n+2:]:
        u, v, c = list(map(int, l.split()))
        if c==-1:
                c=sys.maxsize
        capacity_matrix[u][v]=c
        capacity_matrix[v][u]=c
source = 0
target = len(nodes)-1
flow_value = ford_fulkerson(capacity_matrix, source, target)

t_cut=set(range(54))-s_cut
remove=[]
for a,b in cut:
        if not (a in s_cut and b in t_cut):
                remove.append((a,b))
        if capacity_matrix[a][b]==-1:
                remove.append((a,b))
for r in remove:
        cut.remove(r)
cut = sorted(list(set(cut)))

for a,b in cut:
        print("{} {} {}".format(a,b,capacity_matrix[a][b]))