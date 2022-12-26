from collections import *
N,M = map(int,input().split())
graphs  = defaultdict(list)
for _ in range(M):
    u,v  = map(int,input().split())
    graphs[u-1].append(v-1)
    graphs[v-1].append(u-1)

# print(graphs)
cnt = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if (j in graphs[i]):
                if (k in graphs[j]):
                    if  (i in graphs[k]):
                        cnt += 1
print(cnt)

