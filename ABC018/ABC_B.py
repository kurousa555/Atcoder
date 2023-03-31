from sys import stdin
def func():
    S = list(input())
    N = int(input())
    lenS = len(S)
    for _ in range(N):
        l,r = map(int,stdin.readline().split())
        S[l-1:r] = reversed(S[l-1:r])
    print("".join(S))
func()
func()

