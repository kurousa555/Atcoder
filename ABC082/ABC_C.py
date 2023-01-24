import collections
N = int(input())
a  = list(map(int,input().split()))
A = collections.Counter(a)
ans =  0
for a in A:

    if A[a]>a:ans+=A[a]-a
    elif A[a]<a:ans+=A[a]
    # ans += max(A[a]-a,0)

    
print(ans)
