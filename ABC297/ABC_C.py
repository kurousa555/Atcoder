from sys import stdin
def func():
    H,W  =  map(int,stdin.readline().split())
    S = [list(input()) for _ in range(H)]
    # print(S)
    ans = 0
    for h in  range(H):
        for w  in range(W-1):
            # print(w,S[h][w],S[h][w+1])
            if S[h][w]=="T" and S[h][w+1]=="T":
                ans += 1
                S[h][w] = "P"
                S[h][w+1] = "C"


    for s in S:
        print("".join(s))

    return
func()
