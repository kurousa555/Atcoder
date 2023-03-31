S = list(input())
T  = list(input())
diffs = set()
for i in range(len(S)):
    diff  = (ord(S[i]) - ord(T[i]))%26
    diffs.add(diff)
# print(diffs)
if len(diffs) == 1:
    print("Yes")
else:
    print("No")
