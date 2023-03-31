from sys import stdin
def func():
    N,K = map(int,stdin.readline().split())
    names =  []
    for _ in range(N):
        name = input()
        names.append(name)
    ans = names[:K]
    ans.sort()
    for a in ans:
        print(a)
func()
