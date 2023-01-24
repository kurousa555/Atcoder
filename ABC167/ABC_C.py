import itertools
N,M,X = map(int,input().split())
cost = []
skill =   []
for i in range(N):
    c,*a = list(map(int,input().split()))
    cost.append(c)
    skill.append(a)


ans = []
for num in range(1,1<<N):
    # print(bin(num)[2:].zfill(N))
    tmp = []
    tmp_cost = 0
    for shift in range(N):
        if num>>shift & 1 == 1:
            tmp_cost +=  cost[shift]
            tmp.append(skill[shift])
            # print(tmp_cost)
    # print(tmp)
    tmp = [list(x) for x in zip(*tmp)]


    judge=True
    for i in range(len(tmp)):
        # print(i,sum(tmp[i]))
        if  X>sum(tmp[i]):
            # print(True)
            judge=False
            break
    # print(judge)
    if  judge==True:
        ans.append(tmp_cost)
    # print("="*20)
# print(ans)
if len(ans)==0:print(-1)
else:print(min(ans))
