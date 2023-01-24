N,X = map(int,input().split())
S = list(input())
for s in S:
    if s=="o":X+=1
    if s=="x":X=max(X-1,0)
print(X)
