N = int(input())
S = list(map(int,input().split()))
for a in range(1,1000):
    for b in range(1,1000):
        total = (4*a*b)+(3*a)+(3*b)
        if total > 1000:break
        # print(total)
        if total in S:
            S = [s for s in S if s!=total]
print(len(S))
        

