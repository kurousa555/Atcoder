N = int(input())
binN = list(map(int,list(str(N))))
sumN = sum(binN)
if N%sumN==0:
    print("Yes")
else:
    print("No")
