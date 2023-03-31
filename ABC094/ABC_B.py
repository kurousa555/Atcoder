from sys import stdin
N,M,X = map(int,stdin.readline().split())
A = list(map(int,stdin.readline().split()))
road1 = list(range(X,N))
road2 = list(range(X))
ans1 = 0
ans2 = 0
for r in road1:
    if r in A:ans1+=1
for r in road2:
    if r in A:ans2+=1
# print(road1,road2)
print(min(ans1,ans2))
