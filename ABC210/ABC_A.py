N,A,X,Y = map(int,input().split())
if A>=N:print(A*X)
else:
    print(A*X + (N-A)*Y)
