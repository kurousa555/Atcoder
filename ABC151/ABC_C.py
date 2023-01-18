N,M = map(int,input().split())
judge = [True]*N
WA = [0]*N


for i in range(M):
    p,s =  input().split()
    p = int(p)

    if  judge[p-1] == False:
        continue

    elif judge[p-1] ==  True:
        if s=="WA":
            WA[p-1] += 1
        elif s=="AC":
            judge[p-1]  = False


cnt = 0
for i in range(N):
    if judge[i] == False:cnt+=WA[i]
print(judge.count(False),cnt)
