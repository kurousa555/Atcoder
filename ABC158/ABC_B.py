from sys import stdin
def func():
    N,A,B = map(int,stdin.readline().split())
    ans = 0

    ans += (N//(A+B))*A
    ans += min(N%(A+B),A)
    print(ans)

func()
func()
func()
