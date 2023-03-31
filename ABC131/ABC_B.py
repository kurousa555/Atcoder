from sys import stdin
N,L = map(int,stdin.readline().split())
apples = list(range(L,L+N))
diff = 10000000
ans = None
total = sum(apples)
# print(apples)
for apple in apples:
    tmp_total = total - apple
    tmp_diff = total  - tmp_total
    if abs(tmp_diff) < abs(diff):
        diff = tmp_diff
        ans = tmp_total
print(ans)
