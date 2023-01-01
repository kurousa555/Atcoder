S = tuple(input())
judge = True
i = 0
while judge:
    for s in S:
        print(s,end="")
        i += 1
        if i == 6:judge=False
