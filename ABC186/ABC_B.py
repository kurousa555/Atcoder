H,W = map(int,input().split())
minimum = []
block =  []
for _ in range(H):
    T = list(map(int,input().split()))
    block.append(T)
    minimum.append(min(T))

ans = 0
# print(minimum)
for i in range(H):
    for j in range(W):
        # print(block[i][j])
        ans += block[i][j] -min(minimum)

print(ans)




