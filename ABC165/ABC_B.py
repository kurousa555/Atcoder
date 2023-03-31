N = int(input())
import math

now = 100
ans = 0

while now<N:
    now += now//100
    ans += 1

print(ans)
