from sys import stdin
dy = [1, 0, -1, 0, 1, -1, 1, -1]
dx = [0, 1, 0, -1, 1, 1, -1, -1]
H,W = map(int,stdin.readline().split())
S = [list(input()) for _ in range(H)]
for y in range(H):
    for x in range(W):
        if S[y][x]=="#":continue
        cnt = 0
        for k in  range(8):
            ny = y + dy[k]
            nx = x + dx[k]

            if ny<0 or ny>=H or nx<0 or nx>=W:continue
            if S[ny][nx]=="#":cnt+=1
        S[y][x]=cnt


for s in  S:
    # print("".join(s))
    print(*s,sep="")
