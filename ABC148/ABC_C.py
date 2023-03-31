A,B = map(int,input().split())
for i in range(1,10000000000):
    if (A*i)%B==0:
        print(A*i)
        break

