import itertools
S = list(input())
comb = itertools.permutations(S,3)
print(len(set(comb)))
