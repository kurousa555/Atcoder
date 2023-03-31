from sys import stdin
import math
H,W  = map(int,stdin.readline().split())
A = [list(map(int,stdin.readline().split())) for _ in range(H)]
# comb = math.factorial(H-1+W-1)//math.factorial(H-1)//math.factorial(W-1)
ans = 0

for num in range(1,2**(H+W-2)+1):
    zero_one = list(bin(num)[2:].rjust(H+W-2,"0"))
    come = set()
    come.add(A[0][0])
    x,y=0,0
    for shift in range(H+W-2):
        if 1 & num>>shift == 1:
            # will_move.append(1)
            y += 1
        else:
            # will_move.append(0)
            x += 1
        if x >= W or y>=H:break
        come.add(A[y][x])


    # print(zero_one)
    if H+W-1 == len(come):
        # print(bin(num)[2:],come, True)
        ans+=1
    # else:
    #     print(bin(num))
    #     print(bin(num)[2:],come, False)

    # print(bin(num)[2:])
    # print(will_move)
    # print(x,y)
    # print(come)
print(ans)
