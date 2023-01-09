A,B = map(int,input().split())
S = input()
if S[:A].isdigit():
    if S[A] == "-":
        if S[A+1:].isdigit():
            print("Yes")
            exit()
print("No")
