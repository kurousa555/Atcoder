X = input()
X = X.replace("ch","o")
if len(X)==0:
    print("YES")
    exit()
for x in X:
    if x not in ("o","k","u"):
        print("NO")
        exit()
print("YES")
