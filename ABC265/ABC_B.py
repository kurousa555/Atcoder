N,M,T = map(int,input().split())
A = list(map(int,input().split()))
A = [[a,0] for a in A]

for _ in range(M):
    X,Y = map(int,input().split())
    A[X-1][1] =  Y

for i in range(N-1):
    if T > A[i][0]:
        T -= A[i][0]
        if i != N-2:
            T += A[i+1][1]
    else:
        print("No")
        exit()

else:
    print("Yes")

