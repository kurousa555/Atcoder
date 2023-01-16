from collections import defaultdict
N,M = map(int,input().split())
foods = defaultdict(list)
for i in range(N):
    KA = list(map(int,input().split()))
    K = KA[0]
    A = KA[1:]
    for j in range(K):
        foods[A[j]].append(1)

ans = 0
for i in foods.keys():
    if len(foods[i]) == N:
        ans += 1

print(ans)
        
    

