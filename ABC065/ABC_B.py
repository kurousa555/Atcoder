N = int(input())
botan = [True]+[False]*(N-1)
ans = 0
A = []
for i in range(N):
    A.append(int(input()))

nxt = A[0]
now = 1
for i in range(N):
    # print(nxt,now)
    botan[nxt-1] = True
    botan[now-1] = False

    nxt = A[nxt-1]
    now = A[now-1]
    # print(botan)
    ans += 1
    if botan[1]==True:
        print(ans)
        exit()
# print(A)
print(-1)
# print(botan)
