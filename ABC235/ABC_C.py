
N,Q =  map(int,input().split())
A = list(map(int,input().split()))
# print(A)
for _  in range(Q):
    x,k = map(int,input().split())
    indexes = [i for i, s in enumerate(A) if s == x]
    # print(x,k,indexes)
    if len(indexes)<k:
        print(-1)
    else:    
        print(indexes[k-1]+1)
