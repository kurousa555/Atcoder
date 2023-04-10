from sys import stdin
def func():
    N = int(input())
    C = list(input())
    red_cnt = C.count("R")
    red_set = C[:red_cnt]
    print(red_set.count("W"))
    return
func()
