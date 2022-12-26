H = 21
M = 0
K = int(input())

if K >= 60:
    H += 1
    M = K - 60
else:
    M = K
M = str(M).rjust(2,"0")
print( f"{H}:{M}" )
