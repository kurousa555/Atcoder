N = int(input())
T = [int(input()) for _ in range(N)]
T.sort(reverse=True)
T = set(T)
it = 0
for t in T:
    if it==1:print(t)
    it+=1
