from sys import stdin
H = int(input())
ans = 0
i = 1
def func(h):
    global ans,i
    # print(h,ans)
    if h==1:
        ans +=  i
        return ans
    else:
        ans += i
        i *= 2
        func(h//2)

func(H)
print(ans)
