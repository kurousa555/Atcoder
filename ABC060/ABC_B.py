from sys import stdin
def func():
    A,B,C = map(int,stdin.readline().split())
    mods = set()
    for i in range(1,101):
        mod = (A*i) % B
        mods.add(mod)
    # print(mods)
    if C in mods:
        print("YES")
    else:
        print("NO")
func()
