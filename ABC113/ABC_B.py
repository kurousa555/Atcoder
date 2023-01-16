N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))
ans =  None
ans_abs = float("inf")
for i in range(N):
    tmp = abs((T-H[i]*0.006)-A)
    if  tmp < ans_abs:
        ans_abs = tmp
        ans = i+1
print(ans)


