from sys import stdin
N = int(input())
A = list(map(int,stdin.readline().split()))
A = [[i,a] for i,a in enumerate(A,start=1) ]  
A.sort(key=lambda x:x[1])
for a in A:
    print(a[0],end=" ")
print()
