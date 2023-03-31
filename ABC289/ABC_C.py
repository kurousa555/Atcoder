from sys import stdin
N,M = map(int,stdin.readline().split())
all_N =  set([i for i in  range(1,N+1)])
A = []
ans = 0
for _ in range(M):
    c =  int(input())
    a = set(map(int,stdin.readline().split()))
    A.append(a)
for num in range(1,2**M):
    test_set = set()
    # print(bin(num))
    for shift in range(M):
        if 1&  num>>shift == 1:
            test_set =  test_set | A[shift]
    result  = test_set & all_N
    if len(result) == N:ans+=1
print(ans)

