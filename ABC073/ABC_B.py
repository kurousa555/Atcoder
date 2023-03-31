from sys import stdin
def func():
    N = int(input())
    ans = 0
    for  _ in range(N):
        r,l = map(int,stdin.readline().split())
        ans  += l-r+1
    print(ans)
func()
# func()
# 
