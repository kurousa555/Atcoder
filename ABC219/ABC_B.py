S = []
for _ in range(3):
    S.append(input())
T = list(map(int,input()))
for t in  T:
    print(S[t-1],end="")
print()
