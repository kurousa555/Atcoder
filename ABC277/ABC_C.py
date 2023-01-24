
import collections

N = int(input())
tree = [[] for i in range(N+1)]
tree = collections.defaultdict(list)
for _ in range(N-1):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)
print(tree)

ans  = 1
come = set()
que = collections.deque()
que.append(1)
while len(que)!=0:
    now = que.popleft()
    ans = max(now,ans)
    for to in tree[now]:
        if to not in come:
            que.append(to)
            come.add(to)
print(ans)
