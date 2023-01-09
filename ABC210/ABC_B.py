N = int(input())
S = tuple(input())
bad_idx = S.index("1")+1
if bad_idx%2 == 1:print("Takahashi")
else:print("Aoki")
