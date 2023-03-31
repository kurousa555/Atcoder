from sys import stdin
N =  int(input())
A = list(map(int,stdin.readline().split()))
A = [a-1 for a in  A]
# A.sort()
print(sum(A))
