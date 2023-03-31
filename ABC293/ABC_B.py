from sys import stdin
N = int(input())
X = list(map(int,stdin.readline().split()))
non_res = set(range(1,N+1))
res = set()
for i in range(1,N+1):
    # print(i)
    if i not in res:
        # res.append(i)
        res.add(X[i-1])
    # print(res)

ans = [a for a  in range(1,N+1) if  a  not in res]
print(len(ans))
print(*ans)
