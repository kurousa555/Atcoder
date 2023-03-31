from sys import stdin
N,Q  = map(int,stdin.readline().split())
idxes = list(range(N+1))
balls = list(range(N+1))

# print(idxes)
# print(balls)
for i in range(N):
    x = int(input())
    fi  = idxes[x]
    si = fi+1
    if fi==N:
    idxes[x],idxes[x+1] = idxes[x+1],idxes[x]
    print(idxes)
    print("*"*50)
print(balls)
