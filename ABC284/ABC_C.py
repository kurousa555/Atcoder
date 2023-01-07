from collections import defaultdict, deque


N,M = map(int,input().split())
graph = defaultdict(list)
tops = [i for i in range(1,N+1)]
if M == 0:
    print(N)
    exit()

for i in range(M) :
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)
cnt = 0
while len(tops) != 0:
    que = deque()
    que.append(tops[0])
    S = {tops[0]}

    # print(S, que)
    while que:
        v = que.popleft()
        for i in graph[v]:
            if not i in S:
                que.append(i)
                S.add(i)
        tops.remove(v)
    cnt += 1

print(cnt)
