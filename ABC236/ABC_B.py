import collections
N = int(input())
A = tuple(map(int,input().split()))
num_count = collections.Counter(A)
keys = [k for k, v in num_count.items() if v == 3]
print(*keys)
