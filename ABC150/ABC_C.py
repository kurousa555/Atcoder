from sys import stdin
import itertools
N = int(input())
P = tuple(map(int,stdin.readline().split()))
Q = tuple(map(int,stdin.readline().split()))
dic = list(itertools.permutations(range(1,N+1),N))
print(abs(dic.index(P)-dic.index(Q)))
