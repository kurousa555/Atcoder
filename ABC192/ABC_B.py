S = list(input())
even = "".join(S[1::2])
odd  = "".join(S[0::2])
if len(S)==1:
    if S[0].islower():
        print("Yes")
    else:
        print("No")
else:
    if even.isupper() and odd.islower():
        print("Yes")
    else:
        print("No")

