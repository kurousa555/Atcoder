import collections
N = int(input())
A = tuple(map(int,input().split()))
B = tuple(map(int,input().split()))
ans1 = 0
ans2 = 0

for i in range(N):
    if A[i] == B[i]:ans1 += 1

A_count = collections.Counter(A)
B_count = collections.Counter(B)
# print(A_count,B_count)
for key in tuple(A_count.keys()):
    ans2 += min(A_count[key],B_count[key])
    # print(key,A_count[key],B_count[key])
print(ans1)
print(ans2-ans1)
