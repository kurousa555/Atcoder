N,idx =  map(int,input().split())
A = list(map(int,input().split()))
idx_set = set([idx])

cnt  = 1
for i in range(N):
    idx  = A[idx-1]
    if idx in idx_set:
        print(cnt)
        break
    cnt += 1
    idx_set.add(idx)
