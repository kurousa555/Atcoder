X,Y = map(int,input().split())
if Y<=X:print(0)
else:
    diff = Y-X
    if diff%10==0:print(diff//10)
    else: print(diff//10+1)
