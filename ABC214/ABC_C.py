N = int(input())
S = tuple(map(int,input().split()))
T = tuple(map(int,input().split()))
received = [[]*N for _ in range(N)]

for i in range(0,N-1):
    init = T[i]
    for j in range(i+1,N):
        init += S[j-1]
        received[i].append(init)

for i in range(0,N-1):
    init = T[i] + sum(S[i:N])
    for j in range(i+1):
        init += sum(S[0:j+1])
        received[i].append(init)



for i in range(N):
    received[i].append(T[i])
    print(min(received[i]))
print(min(received))
