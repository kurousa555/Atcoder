import itertools
S = list(input())
N = int(input())
names = list(itertools.product(S, repeat=2))
print("".join(names[N-1]))
