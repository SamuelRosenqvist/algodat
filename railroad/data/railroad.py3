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
                                if v == t:
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
                path = dfs(C,F,s,t)
        return sum(F[s][i] for i in range(n))


with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

n=int(lines[0])
m=int(lines[n+1])
nodes=[]
s_cut=[]
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
print("max flow {}".format(flow_value))
t_cut=set(range(54))-s_cut
min_cut=[]
for e in s_cut:
        for t in t_cut:
                if capacity_matrix[e][t]!=0:
                        min_cut.append((e,t))

for a,b in min_cut:
        print("{} {} {}".format(a,b,capacity_matrix[a][b]))