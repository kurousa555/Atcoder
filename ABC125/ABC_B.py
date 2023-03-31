import itertools
N = int(input())
V = list(map(int,input().split()))
C = list(map(int,input().split()))

ans = []
for num in range(1<<N):
    X,Y = 0,0
    for shift in range(N):
        if num>>shift & 1 == 1:
            X+=V[shift]
            Y+=C[shift]
    ans.append(X-Y)
print(max(ans))
