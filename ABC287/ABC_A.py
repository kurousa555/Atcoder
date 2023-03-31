def judge():
    N = int(input())
    For = 0
    Against = 0
    for _ in range(N):
        S = input()
        if S == "For":For+=1
        if S == "Against":Against+=1
    if For>Against:print("Yes")
    if For<Against:print("No")
judge()
