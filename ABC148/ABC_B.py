N = int(input())
ST = list(map(list,input().split()))
ans = [None]*N*2
ans[::2]=ST[0]
ans[1::2]=ST[1]
print("".join(ans))
