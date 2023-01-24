# 入力の受け取り
N,X,Y=map(int,input().split())

tree = [[] for i in range(N+1)]

for i range(N-1):
        # 入力の受け取り
    U,V=map(int,input().split())
    # 繋がっている頂点の記録
    connect[U].append(V)
    connect[V].append(U)
Dist = [-1]*N
Dist[X]=0
from collections import deque
que=deque()

que.append(X)
while len(que)!=0:
    now = que.popleft()
    for to in connect[Now]:
        if Dist[to] == -1:
            Dist[to]=Dist[Now]+1
            que.append(to)
ans = deque()
Count = Dist[Y]
Now=Y


while 0<Count:
    ans.appendleft(Now)
    for to in connect[Now]:
        if Dist[to]==Count-1:
            Count-=1
            Now=to
