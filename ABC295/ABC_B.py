from sys import stdin
def func():
    R,C = map(int,stdin.readline().split())
    B = [list(input()) for _ in range(R)]
    # dy = [1, 0, -1, 0]
    # dx = [0, 1, 0, -1]
    # print(B)
    for y in range(R):
        for x in range(C):
            if B[y][x].isnumeric():
                width = int(B[y][x])

                for exy in range(R):
                    for exx in range(C):
                        judge  =  abs(y-exy) + abs(x-exx)
                        
                        # if width == 2:print(y,x,exy,exx,B[exy][exx],judge,width)
                        if judge <= width:
                            # print(exy,exx)
                            if B[exy][exx] == "#":
                                # print(exy,exx)
                                B[exy][exx] = "."

                B[y][x] = "."
    for b in B:
        print("".join(b))

func()
