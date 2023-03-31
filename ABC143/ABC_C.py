N = int(input())
S = list(input())
now = None
ans = 0
for s in  S:
    if s != now:
        # print(s,end="")
        ans +=  1
        now =  s
print(ans)
