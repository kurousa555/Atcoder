N = int(input())
S_P = []
for i in range(N):
    S,P = input().split()
    S_P.append([i+1,S,int(P)])

S_P.sort(key=lambda x:(x[1],-(x[2])))
for s_p in S_P:
    print(s_p[0])
