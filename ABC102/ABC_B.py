N = int(input())
A = tuple(map(int,input().split()))
ans = 0
for i in range(N):
    for j in range(i+1,N):
        tmp =  abs(A[i]-A[j])
        if tmp>ans:ans=tmp
print(ans)
