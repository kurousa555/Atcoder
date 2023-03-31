import collections
# def judge():
N,M = map(int,input().split())
tree = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

Dist = [-1]*(N+1)
Dist[1] = 0

come = set()
que = collections.deque()
que.append(1)

judge=False
while len(que) > 0:
    now = que.popleft()
    for to in tree[now]:
        if Dist[to] == -1:
            Dist[to] = Dist[now]+1
            que.append(to)

if Dist[N]==2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
# print(Dist)
# print('POSSIBLE' if judge() else 'IMPOSSIBLE')

