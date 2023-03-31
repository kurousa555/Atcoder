from sys import stdin
N,M,T  =  map(int,stdin.readline().split())
battery=N
now=0

for _ in range(M):
    A,B = map(int,stdin.readline().split())
    battery -= A-now


    if battery<=0:
        print("No")
        exit()
    battery = min(battery+(B-A),N)
    now = B

battery -= T-now
if battery<=0:
    print("No")
    exit()
print("Yes")

