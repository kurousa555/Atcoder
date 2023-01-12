
N = int(input())
A = list(map(int,input().split()))
B = tuple(map(int,input().split()))
ans = 0
for i in range(N):
    leave = 0
    if B[i] > A[i]:
        leave = B[i]-A[i]
        ans += A[i] 
        if leave >= A[i+1]:
            ans += A[i+1]
            A[i+1] = 0
        else:
            ans += leave
            A[i+1] -= leave
    else:
        ans += B[i]
print(ans)
