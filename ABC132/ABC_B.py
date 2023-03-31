n = int(input())
P = list(map(int,input().split()))
ans = 0
for i in range(n-2):
    if P[i]<P[i+1]<P[i+2]:ans+=1
    if P[i+2]<P[i+1]<P[i]:ans+=1
    # print(P[i+1],P[i],P[i-1],P[i+1]<P[i]<P[i-1])
    # print(P[i-1],P[i],P[i+1],P[i-1]<P[i]<P[i+1])
    # print("="*30)
print(ans)
