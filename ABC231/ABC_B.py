import collections
N = int(input())
names = [input() for _ in range(N)]
counter = collections.Counter(names)
counter = sorted(counter.items(), key=lambda x:x[1])
print(counter[-1][0])
