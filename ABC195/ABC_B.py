from sys import stdin
def func():
    A,B,W = map(int,stdin.readline().split())
    W *= 1000
    for _ in range(15):
        W -= B
        print(W)
func()

