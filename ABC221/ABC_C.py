N = input()
lenN = len(N) 

ans = []
for num in range(1<<lenN):
    gpA =  []
    gpB = []
    for shift in range(lenN):
        if (num>>shift) & 1 == 1:
            gpA.append(N[shift])
        if (num>>shift) & 1 != 1:
            gpB.append(N[shift])

    if len(gpA)==0 or len(gpB)==0: continue

    gpA.sort(reverse=True,  key=lambda x:int(x))
    gpB.sort(reverse=True,  key=lambda x:int(x))
    A = int("".join(gpA))
    B = int("".join(gpB))
    ans.append(A*B)
print(max(ans))
