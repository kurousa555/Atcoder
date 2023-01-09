A,B,C = map(int,input().split())

if A>B:print("Takahashi")
if B>A:print("Aoki")
if A==B:
    if C == 1:print("Takahashi")
    if C == 0:print("Aoki")
