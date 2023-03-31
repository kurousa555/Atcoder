from sys import stdin
import collections

N =  int(input())
edge = collections.defaultdict(list)
for _ in range(N):
    a,b = map(int,stdin.readline().split())
    edge[a].append(b)
    edge[b].append(a)

que = collections.deque()
que.append(1)
passage = set()
passage.add(1)
highest = 1

while len(que)>0:
    now = que.popleft()
    for to in edge[now]:
        if to not in passage:
            que.append(to)
            passage.add(to)

print(max(list(passage)))
