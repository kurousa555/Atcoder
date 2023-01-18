S = list(map(int,list(input())))
# print(S)
K = int(input())

if S.count(1)<0 or S.count(1)==len(S):
    print(S[0])
    exit()


for i in range(len(S)):
    if S[i] != 1:
        key_idx = i
        break


if key_idx+1 <= K:
    print(S[key_idx])
elif key_idx+1 > K:
    print(1)


