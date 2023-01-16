N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

for i in range(1,N+1):
    i  = i%N
    T[i] = min(T[i-1]+S[i-1],T[i])
for i in range(1,N+1):
    i  = i%N
    T[i] = min(T[i-1]+S[i-1],T[i])
for t in T:
    print(t)
