def judge():
    S = [input() for _ in range(4)]
    if len(set(S)) == 4:
        return True
    else:
        return False

print("Yes" if judge() else "No")


def judge():
S = [input() for _ in range(4)]
if len(set(S)) == 4:
    print("Yes")
else:
    print("No")

print("Yes" if judge() else "No")

