N = int(input())
res =  0

if N==1:
    print(0)
    exit()

for i in range(10**18):
    if 2**i <= N:
        res = i
    else:
        print(res)
        exit()
