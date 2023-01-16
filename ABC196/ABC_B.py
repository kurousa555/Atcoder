N = list(input())
if N.count(".")==1:
    idx = N.index(".")
    print("".join(N[:idx]))
else:
    print("".join(N))
