N = int(input())
A = list(map(int, input().split()))

import collections
add = collections.defaultdict(int)
Q = int(input())
now = -1
print("🌟"*40)
for _ in range(Q):
    X = list(map(int, input().split()))
    print(X)
    if X[0] == 1:
        now = X[1]
        add = collections.defaultdict(int)
    elif X[0] == 2:
        i, x = X[1]-1, X[2]
        add[i] += x
    else:
        i = X[1] - 1
        if now == -1:
            print(A[i] + add[i])
        else:
            print(now + add[i])
    print(add,now)
    print("="*30)
