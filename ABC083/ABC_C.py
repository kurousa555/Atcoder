x, y = map(int, input().split())

num = x
ans = 0

while (num <= y):
    num *= 2
    ans += 1
    # print(num)

print(ans)
