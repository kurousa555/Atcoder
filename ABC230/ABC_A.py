N = int(input())
if N >= 42:
    N = str(N+1).rjust(3,"0")
else:
    N = str(N).rjust(3,"0")
print(f"AGC{N}")
