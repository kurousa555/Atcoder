n = int(input())
# n=8
origin = [0,0,1]
mod = 10007

if n in (1,2):
    print(0)
else:
    for i in range(n-3):
        origin.append(sum(origin[i:i+3])%mod)
    print(origin[-1])
# print(origin)
