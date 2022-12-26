N,Q = map(int,input().split())
S = input()
diff = 0
for _ in range(Q):
    t,x = map(int,input().split())
    if t == 1: 
        diff += x
        if diff >= N: diff-=N
    elif t == 2:
        total = x-diff
        if  total <= -N: total+=N
        print(S[total-1])
    
