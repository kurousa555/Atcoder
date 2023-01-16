N = int(input())
S =  [list(input()) for  _  in  range(N)]
new_S = [[None]*N for  _  in  range(N)]
for  i in range(N):
    for j in range(N):
        # print(i,j,j,(N-1-i))
        new_S[j][(N-1)-i] = S[i][j]

for ns in new_S:
    print("".join(ns))
