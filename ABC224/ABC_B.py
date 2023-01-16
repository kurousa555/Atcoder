H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
for i in range(H):
    for j in range(i+1,H):

        for k in range(W):
            for l in range(k+1,W):
                if A[i][k]+A[j][l] <= A[j][k]+A[i][l]:
                    pass
                elif A[i][k]+A[j][l] > A[j][k]+A[i][l]:
                    print("No")
                    exit() 
print("Yes")
