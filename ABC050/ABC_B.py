import copy
N = int(input())
T = list(map(int,input().split()))
M =  int(input())

for _  in range(M):
    p,x = map(int,input().split())
    t =  T.copy()
    t[p-1] = x
    print(sum(t))
