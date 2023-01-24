N = int(input())
S = list(input())
if N%2==1:
    print("No")
    exit()
first = S[:N//2]
second = S[N//2:]
if first==second:
    print("Yes")
else:
    print("No")
