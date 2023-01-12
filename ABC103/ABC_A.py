A = list(map(int,input().split()))
A = sorted(A)
cnt  = 0
for i in range(len(A)-1):
    cnt += abs(A[i]-A[i+1])
print(cnt)
