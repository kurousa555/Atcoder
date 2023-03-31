def func():
    N,K = map(int,input().split())
    ans = N
    if N%K==0:
        print(0)
        exit()
    print(min(N%K, abs(N%K-K)))
func()
func()
func()
