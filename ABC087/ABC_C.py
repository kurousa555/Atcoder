N = int(input())
A = [list(map(int,input().split())) for i in range(2)]

res = []
for i in range(N):
    res.append(sum(A[0][:i+1])+sum(A[1][i:]))
print(max(res))
