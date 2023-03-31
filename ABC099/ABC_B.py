from sys import stdin
pools = list(range(1,1001))
a,b = map(int,stdin.readline().split())
pile_diff  = b-a

for i  in range(1,1000):
    pools[i] = pools[i]+pools[i-1]

for i  in range(1,1000):
    height_diff  = abs(pools[i-1]-pools[i])
    if pile_diff==height_diff:
        # print(pools[i-1]-pools[i])
        # print(pools[i-1],pools[i])
        print(abs(a-pools[i-1]))
        break
