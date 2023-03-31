from sys import stdin
import collections

N = int(input())
A = [0]+list(map(int,stdin.readline().split()))
ameba = [0]*(2*N+2)
# print(A)
# print(ameba)
for i in range(1,N+1):
    ameba[2*i] = ameba[A[i]]+1
    ameba[2*i+1] = ameba[A[i]]+1
    
for i in range(1,2*N+2):
    print(ameba[i])
