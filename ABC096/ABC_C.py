dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
from sys import stdin
H,W = map(int,stdin.readline().split())
S = [list(input()) for _ in range(H)]

# print(S)
for y in range(H):
    for  x  in range(W):
        judge = False
        if S[y][x] == ".":
            continue
        
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if ny < 0 or H <= ny\
                    or nx < 0 or W <= nx:
                continue

            if S[ny][nx] == '#':
                judge = True
        if judge==False:
            print("No")
            exit()
print("Yes")




