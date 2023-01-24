N = int(input())
X = list(map(int,input().split()))
newX = sorted(X)
center = sum([newX[N//2],newX[N//2-1]])/2

for i in range(N):
    # print(X[i])
    if X[i]<center:
        print(newX[N//2])
    elif X[i]>center:
        print(newX[N//2-1])
    elif X[i]==center:
        print(int(center))
    

