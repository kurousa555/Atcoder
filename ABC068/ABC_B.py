N  = int(input())
ans = 1
maximum = 0
for i in range(1,N+1):
    div = i
    tmp = 0
    while True:
        if div%2==0 and div!=0:
            div //= 2
            tmp += 1
        else:break
    if tmp > maximum:
        maximum=tmp
        ans = i


print(ans)
