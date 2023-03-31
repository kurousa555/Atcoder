import sys
from sys import stdin
import collections
sys.setrecursionlimit(10 ** 6)
N, M = map(int, input().split())
p = [-1] * N
tree = [[] for _ in range(N+1)]
def root(x):
  if p[x] < 0:
    return x
  p[x] = root(p[x])
  return p[x]
 
def merge(x, y):
  x = root(x)
  y = root(y)
  if x == y:
    return
  p[y] = x
  
deg = [0] * N
for _ in range(M):
  A, B = map(int, input().split())
  tree[A].append(B)
  tree[B].append(A)
  A -= 1
  B -= 1
  deg[A] += 1
  deg[B] += 1
  if root(A) == root(B) or deg[A] > 2 or deg[B] > 2:
    exit(print('No'))
  merge(A, B)
    
que =  collections.deque()
que.append(1)
come = set()

while len(que)>0:
    now = que.popleft()
    come.add(now)
    for to in tree[now]:
        if to not in come:
            que.append(to)
            come.add(to)

if len(come) != N:
    print("No")
    exit()

print("Yes")
