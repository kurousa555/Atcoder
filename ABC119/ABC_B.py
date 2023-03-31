from sys import stdin
N = int(input())
ans = 0
for _ in range(N):
    x,u = stdin.readline().split()
    if u=="JPY":ans+=float(x)
    if u=="BTC":ans+=float(x)*380000.0
print(ans)
