N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
max_A = max(A)
A = [i for i in range(N) if A[i]==max_A ]
for a in (A):
    for b in (B):
        if a == (b-1):
            print("Yes")
            exit()
print("No")
