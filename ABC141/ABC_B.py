S = input()
for i in range(len(S)):
    if i%2==0:
        if S[i] not in ("R","U","D"):
            print("No")
            exit()
    if i%2==1:
        if S[i] not in ("L","U","D"):
            print("No")
            exit()
print("Yes")
