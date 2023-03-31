from sys import stdin
N,K  = map(int,stdin.readline().split())
S = list(input())
lim = 0
for i in range(N):
    if S[i] == "o":lim+=1
    if S[i] == "o" and lim>K:S[i]="x"
print("".join(S))
