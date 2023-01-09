N,R = map(int,input().split())
if N<10:
    print(R + (100*(10-N)))
elif N>=10:
    print(R)
