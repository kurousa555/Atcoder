from sys import stdin
def func():
    N = int(input())
    S = list(stdin.readline().split())
    if len(set(S)) == 3:print("Three")
    if len(set(S)) == 4:print("Four")

func()
func()
func()
