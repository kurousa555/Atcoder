N = int(input())
S = list(input())
ans = []
for i in range(N-2):
    ans.append("".join(S[i:i+3]))
print(ans.count("ABC"))
