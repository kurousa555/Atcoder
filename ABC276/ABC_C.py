import itertools
from sys import stdin
N = int(input())
A =  list(map(int,stdin.readline().split()))
# print(A[-1:-N-1:-1])
# print(A)
for i in range(-1,-N,-1):
    if A[i-1] > A[i]:
        first = A[:N+i-1]
        middle = A[i-1]
        second = A[N+i:]
        # print(first)
        # print(middle)
        # print(second)
        for j in range(middle-1,0,-1):
            if j in second:
                idx = second.index(j)
                middle,second[idx] = second[idx],middle
                break
        # print(first)
        # print(middle)
        # print(second)
        second.sort(reverse=True)
        # print(second)

        print(*first + [middle] + second)


        break
        # if i==-1:break
        # f = A[N-i-1]
        # print(f)
        # A =  list(itertools.permutations(range(1,N+1),N))
# print(A)
# 
