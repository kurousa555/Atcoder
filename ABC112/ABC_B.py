from sys import stdin
def func():
    N,T = map(int,stdin.readline().split())
    c_t = [list(map(int,stdin.readline().split())) for _ in range(N)]
    c_t = [i for i in c_t if i[1]<=T]
    if len(c_t)==0:
        print("TLE")
        exit()
    c_t.sort(key=lambda x:x[0])
    print(c_t[0][0])

# func()
# func()
func()
