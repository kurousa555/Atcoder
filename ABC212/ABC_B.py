N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
AB = []
for a in A:
    AB.append([a,0])
for b in B:
    AB.append([b,1])
AB.sort(key=lambda x: x[0])

ans = 1000000000000
for i in range(N+M-1):
    if AB[i][1] != AB[i+1][1]:
        tmp_ans = abs(AB[i][0]-AB[i+1][0])
        # print(AB[i],AB[i+1],tmp_ans)
        if tmp_ans < ans:ans = tmp_ans

print(ans)
