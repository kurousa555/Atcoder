N = int(input())

S = [tuple(map(int,input())) for _ in range(N)]
distances = [0]*10
print(S)
for i in range(1):
    for j in range(N):
        print(S[j].index(i))

