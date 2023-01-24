N = int(input())
A = list(map(int,input().split()))
maxi = max(A)
A.remove(maxi)
sumA = sum(A)
if maxi < sumA:
    print("Yes")
else:
    print("No")
