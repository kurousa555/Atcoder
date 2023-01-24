N = int(input())
A = list(map(int,input().split()))

for i  in range(N):
    A[i] = [i+1,A[i]]

A.sort(reverse=True,key=lambda x:x[1])

for a in A:
    print(a[0])
