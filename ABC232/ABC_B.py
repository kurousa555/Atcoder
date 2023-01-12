S = list(map(ord,input()))
T  = list(map(ord,input()))
S = [s-96 for s in S]
T = [t-96 for t in T]
axis  = (T[0]-S[0])%96
for i in range(1,len(T)):
    if ((T[i]-S[i])%96) != axis:
        print("No")
        exit()
print("Yes")


