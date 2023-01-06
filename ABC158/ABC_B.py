import math
N,A,B = map(int,input().split())
one_set = ["b"]*A + ["r"]*B

one_set_len = len(one_set)

how_many_set = math.floor(N/one_set_len)
mod = N%one_set_len

just_set = A*how_many_set
mod_set = one_set[0:mod]

cnt = (just_set) + mod_set.count("b")
print(cnt)


