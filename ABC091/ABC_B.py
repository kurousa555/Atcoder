N = int(input())
S= [input() for _ in range(N)]
M = int(input())
T = [input() for _ in range(M)]
words = set(S+T)
maximum = -100000000
for word in words:
    cnt = 0
    for s in S:
        # print(s,word)
        if s == word:cnt+=1
        # print(cnt)
    for t in T:
        # print(s,word)
        if t == word:cnt-=1
        # print(cnt)
    if cnt > maximum:maximum=cnt
    # print("=========")
print(max(maximum,0))

