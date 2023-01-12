A,B = map(tuple,input().split())
short = min(len(A),len(B))
for i in range(-1,-short-1,-1):
    if int(A[i]) + int(B[i]) >= 10:
        print("Hard")
        exit()
print("Easy")
