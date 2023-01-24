
import collections
n, m = map(int,input().split())
Graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    Graph[a].append(b)

print(Graph)
# i 番目の都市からたどり着ける都市を調べるbfs
def bfs(i):
    global ans
    # 未到達で0、到達で1
    visited = [0] * n
    que = collections.deque()
    que.append(i)
    visited[i] = 1
    ans += 1

    while len(que) != 0:
        tar = que.popleft()
        for j in Graph[tar]:
            # 道でつながって都市が未到達ならキューに追加
            if visited[j] == 0:
                que.append(j)
                visited[j] = 1
                ans += 1
                print(i,j,tar,ans,Graph[tar])
    return


ans = 0
for i in range(n):
    bfs(i)

print(ans)

# from collections import defaultdict
# N,M = map(int,input().split())
# edge = defaultdict(list)
# for _ in range(M):
#     a,b =  map(int,input().split())
#     edge[a].append(b)
#     edge[b].append(a)

# print(edge)

# edge_group = []
# come = set()
# def dfs(now):
#     come.add(now)
#     for to in  edge[now]:
#         if to in come:continue
#         dfs(to)

# dfs(1)

