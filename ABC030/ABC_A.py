A,B,C,D =  map(int,input().split())
X = B/A
Y = D/C

if X > Y:print("TAKAHASHI")
elif X < Y:print("AOKI")
else:print("DRAW")
