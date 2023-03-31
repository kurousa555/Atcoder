from sys import stdin
import collections
N = int(input())
A = list(map(int,stdin.readline().split()))
count  = [0]*(N)
A.sort()
A_count = collections.Counter(A)
A = collections.deque((set(A)))
# print(A)
# print(A_count)
for i in range(len(A)):
    nxt = A.popleft()
    # print(nxt, A)
    # num = A_count[nxt]*len(A)
    # print(num)
    count[len(A)]+=A_count[nxt]
    # print(count)
# print(count)
for c in count:
    print(c)
