from sys import stdin
H,W = map(int,stdin.readline().split())
A = [list(input()) for _ in range(H)]
newA1 = []

for hor in range(H):
    if (len(set(A[hor])) != 1) or (len(set(A[hor])) == 1 and A[hor][0] ==  "#"):
        newA1.append(A[hor])

newA1 = [list(x) for x in zip(*newA1)]
newA2 = []

# print(newA1)
for ver in range(W):
    # print(newA1[ver],len(set(newA1[ver])))
    if (len(set(newA1[ver])) != 1) or (len(set(newA1[ver])) == 1 and newA1[ver][0] ==  "#"):
        newA2.append(newA1[ver])

ans = [list(x) for x in zip(*newA2)]
for a in ans:
    print("".join(a))
