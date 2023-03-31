from sys import stdin
def func():
    N = int(input())   
    for _ in range(N):
        a,b = map(int,stdin.readline().split())
        print(a+b)
func()
