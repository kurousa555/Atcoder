from statistics import mode
abc = tuple(map(int,input().split()))
if len(set(abc)) == 1:print(abc[0])
if len(set(abc)) == 3:print(0)
if len(set(abc)) == 2:
    res = mode(abc)
    for i in abc:
        if i != res:print(i)

