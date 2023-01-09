N,X = map(int,input().split())
A = list(map(int,input().split()))
for i in range(1,N+1):
    if i%2==0:A[i-1]-=1

if sum(A) > X:print("No")
if sum(A) <= X:print("Yes")
