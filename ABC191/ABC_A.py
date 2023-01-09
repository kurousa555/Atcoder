N,X = map(int,input().split())
A = tuple(map(int,input().split()))
for a in A:
    if a!=X:
        print(a,end=" ")
