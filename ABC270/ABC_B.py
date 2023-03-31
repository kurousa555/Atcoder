from sys import stdin
goal, wall, hammer = map(int,stdin.readline().split())

if 0<wall<hammer<goal or 0>wall>hammer>goal or 0<wall<goal<hammer or 0>wall>goal>hammer:
    print(-1)
else:
    print(abs(hammer)+abs(hammer-goal))
