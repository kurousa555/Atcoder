from sys import stdin

N = int(input())
A =  list(map(int,stdin.readline().split()))
maxi=A[0]
ans=0
for a in A:
    if a>maxi:
        maxi=a
    else:
        ans += maxi-a
print(ans)

