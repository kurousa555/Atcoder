def get_integral_value_combination(list, target):
    def a(idx, l, r, t):
        if t == sum(l): r.append(l)
        elif t < sum(l): return
        for u in range(idx, len(list)):
            a((u + 1), l + [list[u]], r, t)
        return r
    return a(0, [], [], target)

def func():
    import math
    N,X = map(int,input().split())
    AB = list(list(map(int,input().split())) for _ in range(N))
    moneys=[0]*N
    for i in range(N):
        for j in range(1,AB[i][1]+1):
            moneys[i] += AB[i][0]

            judge = get_integral_value_combination(moneys,X)
            print(moneys,judge)
            if len(judge)>=1:
                print("Yes")
                exit()
func()
print("No")
    # # 2 19
    # # 2 3
    # # 5 6
