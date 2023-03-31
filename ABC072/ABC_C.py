from sys import stdin
import collections
N =  int(input())
A = list(map(int,stdin.readline().split())) 
for i in range(N):
    A.append(A[i]+1)
    A.append(A[i]-1)
new_A = list(collections.Counter(A).items())
new_A.sort(reverse=True,key=lambda x:x[1])
print(new_A[0][1])

