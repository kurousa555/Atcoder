H,W,X,Y = map(int,input().split())
S = [list(input()) for _ in range(H)]

cnt = 0
right = S[X-1][Y:]
left = list(reversed(S[X-1][:Y-1]))
top = list(reversed([S[i][Y-1] for i in range(H)][:X-1]))
bottom = [S[i][Y-1] for i in range(H)][X:]
cnt = 0

# print(right)
# print(left)
# print(top)
# print(bottom)
for r in right:
    if r==".":cnt+=1
    else:break
for l in left:
    if l==".":cnt+=1
    else:break

for t in top:
    if t==".":cnt+=1
    else:break
for b in bottom:
    if b==".":cnt+=1
    else:break
# print(right)
# print(left)
# print(top)
# print(bottom) 

# print("="*10)
# for s in S:
#     print(s)
print(cnt+1)
