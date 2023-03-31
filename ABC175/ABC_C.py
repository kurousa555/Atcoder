from sys import stdin
X,K,D = map(int,stdin.readline().split())
X =  abs(X)
if X==0 and K%2==0:
    print(0)
elif X==0 and K%2==1:
    print(abs(D))
elif X >= K*D:
    print(X - K*D) 
    # print(1)
else:    
    newX = X - (X//D)*D
    K -= (X//D)
    if X==0:
        print(X)
    else:
        if K%2==0:
            print(newX)
            # print(2)
        if K%2==1:
            # print(X,D)
            print(abs(newX-D))
            # print(3)
